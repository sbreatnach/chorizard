import dataclasses
import enum
import logging
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional

import requests

logger = logging.getLogger(__name__)


class Reference:
    reference_type: str
    reference_id: str


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


class PermissionEvaluation(enum.Enum):
    NoPermission = "PERMISSIONSHIP_NO_PERMISSION"
    HasPermission = "PERMISSIONSHIP_HAS_PERMISSION"
    ConditionalPermission = "PERMISSIONSHIP_CONDITIONAL_PERMISSION"


class RelationshipOperation(enum.Enum):
    Update = "TOUCH"
    Create = "CREATE"
    Delete = "DELETE"


class SpiceDbApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def make_request(self, url, data, **_kwargs):
        full_url = f"{self.base_url}{url}"
        logger.info("SpiceDB request: %s", full_url)
        logger.info("SpiceDB request data: %s", data)
        # every SpiceDB API request is a POST so no need to make it configurable
        response = requests.request("post", full_url, json=data)
        logger.debug("SpiceDB response: %s %s", response.status_code, response.content)
        if response.status_code == HTTPStatus.OK:
            return response.json()
        logger.error("Spice DB error: %s %s", response.status_code, response.content)
        response.raise_for_status()

    def determine_consistency(
        self,
        minimize_latency=None,
        at_least_as_fresh=None,
        at_exact_snapshot=None,
        fully_consistent=None,
        **_kwargs,
    ):
        consistency = {}
        if fully_consistent is not None:
            # TODO: populate
            pass
        if not consistency and at_exact_snapshot is not None:
            # TODO: populate
            pass
        if not consistency and at_least_as_fresh is not None:
            # TODO: populate
            pass
        if not consistency:
            consistency["minimizeLatency"] = (
                minimize_latency if minimize_latency is not None else True
            )
        return consistency

    def save_relationship(
        self,
        relationship: Relationship,
        operation=RelationshipOperation.Create,
        **kwargs,
    ):
        return self.save_relationships([relationship], operation=operation, **kwargs)

    def save_relationships(
        self,
        relationships: list[Relationship],
        operation=RelationshipOperation.Create,
        **kwargs,
    ):
        payload = {
            "updates": [
                {
                    "operation": operation.value,
                    "relationship": dataclasses.asdict(relationship),
                }
                for relationship in relationships
            ]
        }
        return self.make_request("/v1/relationships/write", payload, **kwargs)

    def check_permission(self, permission: Permission, **kwargs):
        payload = dataclasses.asdict(permission)
        payload["consistency"] = self.determine_consistency(**kwargs)
        response = self.make_request("/v1/permissions/check", payload, **kwargs)
        return response["permissionship"] == PermissionEvaluation.HasPermission.value
