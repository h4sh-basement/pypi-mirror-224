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
from pydantic import BaseModel, Field, StrictStr

class ExternalTracker(BaseModel):
    """
    ExternalTracker represents settings for external tracker
    """
    external_tracker_format: Optional[StrictStr] = Field(None, description="External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index.")
    external_tracker_regexp_pattern: Optional[StrictStr] = Field(None, description="External Issue Tracker issue regular expression")
    external_tracker_style: Optional[StrictStr] = Field(None, description="External Issue Tracker Number Format, either `numeric`, `alphanumeric`, or `regexp`")
    external_tracker_url: Optional[StrictStr] = Field(None, description="URL of external issue tracker.")
    __properties = ["external_tracker_format", "external_tracker_regexp_pattern", "external_tracker_style", "external_tracker_url"]

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
    def from_json(cls, json_str: str) -> ExternalTracker:
        """Create an instance of ExternalTracker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalTracker:
        """Create an instance of ExternalTracker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalTracker.parse_obj(obj)

        _obj = ExternalTracker.parse_obj({
            "external_tracker_format": obj.get("external_tracker_format"),
            "external_tracker_regexp_pattern": obj.get("external_tracker_regexp_pattern"),
            "external_tracker_style": obj.get("external_tracker_style"),
            "external_tracker_url": obj.get("external_tracker_url")
        })
        return _obj


