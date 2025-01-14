# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.35
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PersonaToken(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    persona: StrictStr = Field(...)
    object_id: Optional[StrictStr] = Field(None, alias="objectId", description="Optional limitation on a specific object.")
    token: StrictStr = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    expire_at: datetime = Field(..., alias="expireAt")
    __properties = ["id", "persona", "objectId", "token", "createdAt", "expireAt"]

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
    def from_json(cls, json_str: str) -> PersonaToken:
        """Create an instance of PersonaToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                          },
                          exclude_none=True)
        # set to None if object_id (nullable) is None
        # and __fields_set__ contains the field
        if self.object_id is None and "object_id" in self.__fields_set__:
            _dict['objectId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaToken:
        """Create an instance of PersonaToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaToken.parse_obj(obj)

        _obj = PersonaToken.parse_obj({
            "id": obj.get("id"),
            "persona": obj.get("persona"),
            "object_id": obj.get("objectId"),
            "token": obj.get("token"),
            "created_at": obj.get("createdAt"),
            "expire_at": obj.get("expireAt")
        })
        return _obj

