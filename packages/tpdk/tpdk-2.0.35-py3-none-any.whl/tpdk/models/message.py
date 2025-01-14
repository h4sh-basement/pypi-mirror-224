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

class Message(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    dispute: Optional[StrictStr] = None
    agent: Optional[StrictStr] = None
    var_from: Optional[StrictStr] = Field(None, alias="from")
    to: Optional[StrictStr] = None
    body: StrictStr = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    __properties = ["id", "dispute", "agent", "from", "to", "body", "createdAt"]

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
    def from_json(cls, json_str: str) -> Message:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                          },
                          exclude_none=True)
        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if agent (nullable) is None
        # and __fields_set__ contains the field
        if self.agent is None and "agent" in self.__fields_set__:
            _dict['agent'] = None

        # set to None if var_from (nullable) is None
        # and __fields_set__ contains the field
        if self.var_from is None and "var_from" in self.__fields_set__:
            _dict['from'] = None

        # set to None if to (nullable) is None
        # and __fields_set__ contains the field
        if self.to is None and "to" in self.__fields_set__:
            _dict['to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Message:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Message.parse_obj(obj)

        _obj = Message.parse_obj({
            "id": obj.get("id"),
            "dispute": obj.get("dispute"),
            "agent": obj.get("agent"),
            "var_from": obj.get("from"),
            "to": obj.get("to"),
            "body": obj.get("body"),
            "created_at": obj.get("createdAt")
        })
        return _obj

