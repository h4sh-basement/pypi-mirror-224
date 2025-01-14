# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.2
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class Address(BaseModel):
    """
    Address
    """
    street_address: StrictStr = Field(..., alias="streetAddress")
    street_address2: Optional[StrictStr] = Field(None, alias="streetAddress2")
    city: StrictStr = Field(...)
    country: StrictStr = Field(...)
    post_code: StrictStr = Field(..., alias="postCode")
    __properties = ["streetAddress", "streetAddress2", "city", "country", "postCode"]

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
    def from_json(cls, json_str: str) -> Address:
        """Create an instance of Address from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Address:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Address.parse_obj(obj)

        _obj = Address.parse_obj({
            "street_address": obj.get("streetAddress"),
            "street_address2": obj.get("streetAddress2"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "post_code": obj.get("postCode")
        })
        return _obj

