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
from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist

class CreatePullRequestOption(BaseModel):
    """
    CreatePullRequestOption options when creating a pull request
    """
    assignee: Optional[StrictStr] = None
    assignees: Optional[conlist(StrictStr)] = None
    base: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    head: Optional[StrictStr] = None
    labels: Optional[conlist(StrictInt)] = None
    milestone: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    __properties = ["assignee", "assignees", "base", "body", "due_date", "head", "labels", "milestone", "title"]

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
    def from_json(cls, json_str: str) -> CreatePullRequestOption:
        """Create an instance of CreatePullRequestOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreatePullRequestOption:
        """Create an instance of CreatePullRequestOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreatePullRequestOption.parse_obj(obj)

        _obj = CreatePullRequestOption.parse_obj({
            "assignee": obj.get("assignee"),
            "assignees": obj.get("assignees"),
            "base": obj.get("base"),
            "body": obj.get("body"),
            "due_date": obj.get("due_date"),
            "head": obj.get("head"),
            "labels": obj.get("labels"),
            "milestone": obj.get("milestone"),
            "title": obj.get("title")
        })
        return _obj


