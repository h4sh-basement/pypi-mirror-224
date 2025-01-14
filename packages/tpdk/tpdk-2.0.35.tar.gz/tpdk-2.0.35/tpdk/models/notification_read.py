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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class NotificationRead(BaseModel):
    """
    
    """
    type: Optional[StrictStr] = None
    seen: StrictBool = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    __properties = ["type", "seen", "createdAt"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DISPUTE_STATE_UPDATE', 'MESSAGE_SENT', 'DISPUTE_SETTLEMENT', 'DISPUTE_ARBITRATION_REQUIRED', 'DISPUTE_RESOLVED'):
            raise ValueError("must be one of enum values ('DISPUTE_STATE_UPDATE', 'MESSAGE_SENT', 'DISPUTE_SETTLEMENT', 'DISPUTE_ARBITRATION_REQUIRED', 'DISPUTE_RESOLVED')")
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
    def from_json(cls, json_str: str) -> NotificationRead:
        """Create an instance of NotificationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationRead:
        """Create an instance of NotificationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationRead.parse_obj(obj)

        _obj = NotificationRead.parse_obj({
            "type": obj.get("type"),
            "seen": obj.get("seen"),
            "created_at": obj.get("createdAt")
        })
        return _obj

