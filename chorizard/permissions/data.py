from dataclasses import dataclass
from typing import Optional

__all__ = [
    "Permission",
    "Reference",
    "Relationship",
    "RelationshipFilter",
    "Subject",
    "as_reference",
]


@dataclass
class Reference:
    reference_type: str
    reference_id: str


@dataclass
class Subject:
    object: Reference
    optional_relation: Optional[str]


@dataclass
class Relationship:
    resource: Reference
    relation: str
    subject: Subject
    caveat: Optional[dict]


@dataclass
class Permission:
    resource: Reference
    permission: str
    subject: Subject
    context: Optional[dict]


@dataclass
class RelationFilter:
    relation: str


@dataclass
class SubjectFilter:
    subject_type: str
    optional_subject_id: Optional[str]
    optional_relation: Optional[RelationFilter]


@dataclass
class RelationshipFilter:
    resource_type: str
    optional_resource_id: Optional[str]
    optional_relation: Optional[str]
    optional_subject_filter: Optional[SubjectFilter]


def as_reference(reference_mapping, model_instance):
    return Reference(
        reference_type=reference_mapping.get(model_instance.__class__),
        reference_id=str(model_instance.id),
    )
