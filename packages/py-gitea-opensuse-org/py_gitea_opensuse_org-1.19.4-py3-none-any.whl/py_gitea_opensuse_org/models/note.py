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
from pydantic import BaseModel, StrictStr
from py_gitea_opensuse_org.models.commit import Commit

class Note(BaseModel):
    """
    Note contains information related to a git note
    """
    commit: Optional[Commit] = None
    message: Optional[StrictStr] = None
    __properties = ["commit", "message"]

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
    def from_json(cls, json_str: str) -> Note:
        """Create an instance of Note from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Note:
        """Create an instance of Note from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Note.parse_obj(obj)

        _obj = Note.parse_obj({
            "commit": Commit.from_dict(obj.get("commit")) if obj.get("commit") is not None else None,
            "message": obj.get("message")
        })
        return _obj


