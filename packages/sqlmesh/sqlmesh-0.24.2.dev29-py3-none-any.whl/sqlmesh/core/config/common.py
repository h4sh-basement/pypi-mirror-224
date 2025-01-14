from __future__ import annotations

import typing as t
from enum import Enum

from pydantic import validator

from sqlmesh.utils import classproperty
from sqlmesh.utils.errors import ConfigError


class EnvironmentSuffixTarget(str, Enum):
    SCHEMA = "schema"
    TABLE = "table"

    @property
    def is_schema(self) -> bool:
        return self == EnvironmentSuffixTarget.SCHEMA

    @property
    def is_table(self) -> bool:
        return self == EnvironmentSuffixTarget.TABLE

    @classproperty
    def default(cls) -> EnvironmentSuffixTarget:
        return EnvironmentSuffixTarget.SCHEMA


def _concurrent_tasks_validator(v: t.Any) -> int:
    if isinstance(v, str):
        v = int(v)
    if not isinstance(v, int) or v <= 0:
        raise ConfigError(
            f"The number of concurrent tasks must be an integer value greater than 0. '{v}' was provided"
        )
    return v


concurrent_tasks_validator = validator(
    "backfill_concurrent_tasks",
    "ddl_concurrent_tasks",
    "concurrent_tasks",
    pre=True,
    allow_reuse=True,
    check_fields=False,
)(_concurrent_tasks_validator)


def _http_headers_validator(v: t.Any) -> t.Any:
    if isinstance(v, dict):
        return [(key, value) for key, value in v.items()]
    return v


http_headers_validator = validator(
    "http_headers",
    pre=True,
    allow_reuse=True,
    check_fields=False,
)(_http_headers_validator)
