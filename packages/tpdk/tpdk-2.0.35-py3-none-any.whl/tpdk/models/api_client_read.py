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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator

class ApiClientRead(BaseModel):
    """
    
    """
    identifier: constr(strict=True, max_length=32) = Field(...)
    created_at: datetime = Field(..., alias="createdAt")
    scopes: Optional[conlist(StrictStr)] = None
    name: Optional[StrictStr] = None
    __properties = ["identifier", "createdAt", "scopes", "name"]

    @validator('scopes')
    def scopes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('DISPUTE_READ', 'DISPUTE_WRITE', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH', 'OFFER_READ', 'OFFER_WRITE', 'ORGANIZATION_READ', 'INTERNAL_WRITE'):
                raise ValueError("each list item must be one of ('DISPUTE_READ', 'DISPUTE_WRITE', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH', 'OFFER_READ', 'OFFER_WRITE', 'ORGANIZATION_READ', 'INTERNAL_WRITE')")
        return value

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
    def from_json(cls, json_str: str) -> ApiClientRead:
        """Create an instance of ApiClientRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiClientRead:
        """Create an instance of ApiClientRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiClientRead.parse_obj(obj)

        _obj = ApiClientRead.parse_obj({
            "identifier": obj.get("identifier"),
            "created_at": obj.get("createdAt"),
            "scopes": obj.get("scopes"),
            "name": obj.get("name")
        })
        return _obj

