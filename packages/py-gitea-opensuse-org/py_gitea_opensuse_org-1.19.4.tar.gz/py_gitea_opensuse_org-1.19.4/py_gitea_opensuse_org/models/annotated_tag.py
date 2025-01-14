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
from py_gitea_opensuse_org.models.annotated_tag_object import AnnotatedTagObject
from py_gitea_opensuse_org.models.commit_user import CommitUser
from py_gitea_opensuse_org.models.payload_commit_verification import PayloadCommitVerification

class AnnotatedTag(BaseModel):
    """
    AnnotatedTag represents an annotated tag
    """
    message: Optional[StrictStr] = None
    object: Optional[AnnotatedTagObject] = None
    sha: Optional[StrictStr] = None
    tag: Optional[StrictStr] = None
    tagger: Optional[CommitUser] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
    __properties = ["message", "object", "sha", "tag", "tagger", "url", "verification"]

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
    def from_json(cls, json_str: str) -> AnnotatedTag:
        """Create an instance of AnnotatedTag from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tagger
        if self.tagger:
            _dict['tagger'] = self.tagger.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotatedTag:
        """Create an instance of AnnotatedTag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotatedTag.parse_obj(obj)

        _obj = AnnotatedTag.parse_obj({
            "message": obj.get("message"),
            "object": AnnotatedTagObject.from_dict(obj.get("object")) if obj.get("object") is not None else None,
            "sha": obj.get("sha"),
            "tag": obj.get("tag"),
            "tagger": CommitUser.from_dict(obj.get("tagger")) if obj.get("tagger") is not None else None,
            "url": obj.get("url"),
            "verification": PayloadCommitVerification.from_dict(obj.get("verification")) if obj.get("verification") is not None else None
        })
        return _obj


