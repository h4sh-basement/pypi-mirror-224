import ast
import os
from types import FunctionType
from typing import Dict, List, Optional, Sequence, Set, Tuple, Type, Union

import airfly
import regex as re
from airfly._vendor import collect_airflow_operators
from airfly.utils import blacking, isorting, qualname
from asttrs import (
    Assign,
    BinOp,
    Call,
    Comment,
    Constant,
    Expr,
    ImportFrom,
    Load,
    Module,
    Name,
    Pass,
    RShift,
    Store,
    With,
    alias,
    keyword,
    stmt,
    withitem,
)

from .base import BaseTask, TaskTree, Workflow

available_operators = collect_airflow_operators()


class AirflowTask(BaseTask):

    operator_class: Union[Type, str] = "DummyOperator"
    params: Dict[str, Union[FunctionType, str]] = None

    @classmethod
    def _resolve_operator(cls) -> Optional[Type]:

        op = cls.operator_class

        if isinstance(op, str):
            basename = op

        elif isinstance(op, type):
            basename = qualname(op, level=1)

        else:
            return

        items = available_operators[basename]

        if len(items) > 1:
            raise ValueError()  # TODO:

        return items[0]

    @classmethod
    def _resolve_dependency_from_params(
        cls, obj: Union[Dict, List] = None
    ) -> List[Union[FunctionType, Type]]:

        deps = []

        if isinstance(obj, type(None)):

            params = cls.params or {}

            deps.extend(cls._resolve_dependency_from_params(params))

        elif isinstance(obj, str):
            return []

        elif isinstance(obj, (Sequence, Set, Dict)):

            iterator = (
                (el for el in obj)
                if isinstance(obj, (Sequence, Set))
                else (v for _, v in obj.items())
            )

            for el in iterator:
                if isinstance(el, (str, type(None))):
                    continue

                elif isinstance(el, (Sequence, Set, Dict)):  # NOTE: list, tuple, set
                    deps.extend(cls._resolve_dependency_from_params(el))

                elif isinstance(el, FunctionType):
                    deps.append(el)

        return list(set(deps))

    @classmethod
    def collect_dep_stmts(cls) -> List[stmt]:
        """Collect all stmts for all dependencies"""

        param_deps = cls._resolve_dependency_from_params()
        op_dev = cls._resolve_operator()

        op_modname, op_basename = qualname(op_dev).rsplit(".", 1)
        op_modname = op_modname.replace("airfly._vendor.", "")

        dep_stmts = [ImportFrom(module=op_modname, names=[alias(name=op_basename)])]

        for dep in param_deps:
            fn_modname, fn_basename = qualname(dep).rsplit(".", 1)
            dep_stmts.append(
                ImportFrom(module=fn_modname, names=[alias(name=fn_basename)])
            )

        return dep_stmts

    @classmethod
    def to_stmt(cls) -> stmt:

        op = cls._resolve_operator()
        op_name = qualname(op)

        _, op_basename = op_name.rsplit(".", 1)

        task_id = qualname(cls)
        task_varname = task_id.replace(".", "_")

        avai_params = {}
        for base in op.mro()[::-1]:
            avai_params.update(getattr(base, "__annotations__", {}))

        params = dict(task_id=task_id)

        for k, v in (cls.params or {}).items():
            if k in avai_params:
                params.update({k: v})

        assign = Assign(
            targets=[Name(id=task_varname, ctx=Store())],
            value=Call(
                func=Name(id=op_basename, ctx=Load()),
                keywords=[
                    keyword(
                        arg=k,
                        value=(
                            Name(id=qualname(v, level=1), ctx=Load())
                            if isinstance(v, FunctionType)
                            else Constant(value=v)  # TODO: handle callable and lambda
                        ),
                    )
                    for k, v in params.items()
                ],
            ),
        )

        return assign


class AirflowDAG(Workflow):

    _default_header = (
        f"This file is auto-generated by {airfly.__name__} {airfly.__version__}"
    )

    def __init__(
        self,
        name: str,
        tasktree: TaskTree,
        includes: Union[str, List[str]] = None,
        dag_params: Tuple[Optional[str], Optional[str]] = None,
    ):

        self._name = name
        self._tasktree = tasktree
        self._includes = includes
        self._dag_params = dag_params

        self._imports = []

    def to_module(self) -> Module:

        body = (
            [self._build_header()]
            + self._build_imports()
            + self._build_includes()
            + [self._build_dag_context()]
        )

        return Module(body=body)

    def render(self, formatted: bool = True) -> str:
        src = re.sub("\n+", "\n", self.to_module().to_source())

        return isorting(blacking(src)) if formatted else src

    def _build_includes(self) -> List[stmt]:

        if self._includes:
            includes = self._includes
            if isinstance(includes, str):
                includes = [includes]

            imports = []
            statements = []

            for path in includes:
                for st in self._insert_from_pyfile(path):
                    if isinstance(st, (ast.Import, ast.ImportFrom)):
                        if st not in imports:
                            imports.append(st)
                    else:

                        statements.append(st)

            body = (
                imports
                + statements
                + [Comment(body="<" * 10 + " End of code insertion")]
            )

        else:
            body = ast.parse("").body

        return body

    def _build_header(self, header: str = None) -> stmt:
        return Comment(body=header if isinstance(header, str) else self._default_header)

    def _parse_dag_params_from_pyfile(
        self, dag_params: Tuple[Optional[str], Optional[str]]
    ) -> List[keyword]:

        try:
            param_file, param_var = self._dag_params

            if os.path.isfile(param_file):

                with open(param_file) as f:
                    mod = ast.parse(f.read().strip())

                for st in mod.body:
                    if isinstance(st, ast.Assign) and st.targets[0].id == param_var:
                        if isinstance(st.value, ast.Dict) or (
                            isinstance(st.value, ast.Call)
                            and st.value.func.id == "dict"
                        ):

                            return [
                                keyword(arg=None, value=Name(id=param_var, ctx=Load()))
                            ]

        except Exception:
            pass  # TODO: logging

        return []

    def _build_dag_context(self) -> stmt:

        keywords = self._parse_dag_params_from_pyfile(self._dag_params)

        return With(
            items=[
                withitem(
                    context_expr=Call(
                        func=Name(id="DAG", ctx=Load()),
                        args=[Constant(value=self._name)],
                        keywords=keywords,
                    ),
                    optional_vars=Name(id="dag", ctx=Store()),
                )
            ],
            body=self._build_dag_body(),
        )

    def _build_dag_body(self) -> List[stmt]:
        body = []

        taskclass: AirflowTask
        for taskclass in sorted(self._tasktree.taskset, key=lambda el: qualname(el)):
            body.append(taskclass.to_stmt())

        for pair in sorted(
            self._tasktree.taskpairs,
            key=lambda el: f"{qualname(el.up)}{qualname(el.down)}",
        ):
            up: AirflowTask = pair.up
            down: AirflowTask = pair.down
            up_stmt: Assign = up.to_stmt()
            down_stmt: Assign = down.to_stmt()
            body.append(
                Expr(
                    value=BinOp(
                        left=Name(id=up_stmt.targets[0], ctx=Store()),
                        op=RShift(),
                        right=Name(id=down_stmt.targets[0], ctx=Load()),
                    )
                )
            )

        return body if body else [Pass()]

    def _build_imports(self) -> List[stmt]:

        imports = [ImportFrom(module="airflow.models", names=[alias(name="DAG")])]

        taskclass: AirflowTask
        for taskclass in self._tasktree.taskset:
            for st in taskclass.collect_dep_stmts():
                if st not in imports:
                    imports.append(st)

        return imports

    def _insert_from_pyfile(self, path: str) -> List[stmt]:

        try:

            if os.path.isfile(path):

                with open(path) as f:
                    mod = ast.parse(f.read().strip())

                mod.body.insert(0, Comment(body=">" * 10 + f" Include from '{path}'"))

                return mod.body

        except Exception:
            # TODO: logging?
            pass

        return []
