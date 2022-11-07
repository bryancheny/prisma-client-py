from typing import Set
from typing_extensions import Literal, TypedDict, get_args

from pydantic import BaseModel


DatabaseFeature = Literal[
    'enum',
    'json',
    'arrays',
    'decimal',
    'raw_queries',
    'create_many',
    'composite_keys',
    'case_sensitivity',
]


class IDDeclarations(TypedDict):
    cuid: str
    autoincrement: str


class DatabaseConfig(BaseModel):
    id: str
    name: str
    env_var: str
    bools_are_ints: bool
    id_declarations: IDDeclarations
    unsupported_features: Set[DatabaseFeature]

    # TODO: run this under coverage
    def supports_feature(
        self, feature: DatabaseFeature
    ) -> bool:  # pragma: no cover
        if feature not in get_args(DatabaseFeature):
            raise RuntimeError(f'Unknown feature: {feature}')

        return feature not in self.unsupported_features
