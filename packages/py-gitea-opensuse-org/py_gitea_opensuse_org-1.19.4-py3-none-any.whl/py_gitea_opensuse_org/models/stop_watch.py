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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class StopWatch(BaseModel):
    """
    StopWatch represent a running stopwatch
    """
    created: Optional[datetime] = None
    duration: Optional[StrictStr] = None
    issue_index: Optional[StrictInt] = None
    issue_title: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    repo_owner_name: Optional[StrictStr] = None
    seconds: Optional[StrictInt] = None
    __properties = ["created", "duration", "issue_index", "issue_title", "repo_name", "repo_owner_name", "seconds"]

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
    def from_json(cls, json_str: str) -> StopWatch:
        """Create an instance of StopWatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StopWatch:
        """Create an instance of StopWatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StopWatch.parse_obj(obj)

        _obj = StopWatch.parse_obj({
            "created": obj.get("created"),
            "duration": obj.get("duration"),
            "issue_index": obj.get("issue_index"),
            "issue_title": obj.get("issue_title"),
            "repo_name": obj.get("repo_name"),
            "repo_owner_name": obj.get("repo_owner_name"),
            "seconds": obj.get("seconds")
        })
        return _obj


