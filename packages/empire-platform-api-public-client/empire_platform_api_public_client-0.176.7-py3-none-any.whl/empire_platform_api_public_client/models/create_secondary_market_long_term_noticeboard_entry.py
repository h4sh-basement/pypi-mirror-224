# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.176.7
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictInt, confloat, conint
from empire_platform_api_public_client.models.border_direction import BorderDirection
from empire_platform_api_public_client.models.noticeboard_entry_type import NoticeboardEntryType

class CreateSecondaryMarketLongTermNoticeboardEntry(BaseModel):
    """
    CreateSecondaryMarketLongTermNoticeboardEntry
    """
    type: NoticeboardEntryType = Field(...)
    first_day: date = Field(..., alias="firstDay", description="One single calendar day, interpreted in **System Time**  - ISO 8601 compliant string in `yyyy-mm-dd` format ")
    last_day: date = Field(..., alias="lastDay", description="One single calendar day, interpreted in **System Time**  - ISO 8601 compliant string in `yyyy-mm-dd` format ")
    direction: BorderDirection = Field(...)
    notice_capacity: StrictInt = Field(..., alias="noticeCapacity", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    notice_price: Union[confloat(multiple_of=0.01, strict=True), conint(strict=True)] = Field(..., alias="noticePrice", description="Currency value in Euros (€), accepted with a precision of maximum 2 decimal places")
    expiry_date: Optional[datetime] = Field(None, alias="expiryDate", description="Date and time with zone information, marks an **absolute point** on the timeline  - theoretically can be sent and received with any zone offset (until it marks the desired **absolute point** on the timeline) - in practice it is advised to transfer it in UTC timezone (with Z offset, \"Zulu time\") - ISO 8601 compliant string in `yyyy-mm-ddThh:mm:ss.SSSZ` format ")
    __properties = ["type", "firstDay", "lastDay", "direction", "noticeCapacity", "noticePrice", "expiryDate"]

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
    def from_json(cls, json_str: str) -> CreateSecondaryMarketLongTermNoticeboardEntry:
        """Create an instance of CreateSecondaryMarketLongTermNoticeboardEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSecondaryMarketLongTermNoticeboardEntry:
        """Create an instance of CreateSecondaryMarketLongTermNoticeboardEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSecondaryMarketLongTermNoticeboardEntry.parse_obj(obj)

        _obj = CreateSecondaryMarketLongTermNoticeboardEntry.parse_obj({
            "type": obj.get("type"),
            "first_day": obj.get("firstDay"),
            "last_day": obj.get("lastDay"),
            "direction": obj.get("direction"),
            "notice_capacity": obj.get("noticeCapacity"),
            "notice_price": obj.get("noticePrice"),
            "expiry_date": obj.get("expiryDate")
        })
        return _obj

