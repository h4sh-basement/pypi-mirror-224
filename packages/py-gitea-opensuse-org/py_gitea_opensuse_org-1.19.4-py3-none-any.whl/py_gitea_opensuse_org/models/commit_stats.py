# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.19.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt

class CommitStats(BaseModel):
    """
    CommitStats is statistics for a RepoCommit
    """
    additions: Optional[StrictInt] = None
    deletions: Optional[StrictInt] = None
    total: Optional[StrictInt] = None
    __properties = ["additions", "deletions", "total"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CommitStats:
        """Create an instance of CommitStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommitStats:
        """Create an instance of CommitStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommitStats.parse_obj(obj)

        _obj = CommitStats.parse_obj({
            "additions": obj.get("additions"),
            "deletions": obj.get("deletions"),
            "total": obj.get("total")
        })
        return _obj


