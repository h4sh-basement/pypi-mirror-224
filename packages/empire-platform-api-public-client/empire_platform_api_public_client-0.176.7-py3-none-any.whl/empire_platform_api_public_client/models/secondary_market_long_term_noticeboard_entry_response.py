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

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictInt, StrictStr, confloat, conint, constr, validator

class SecondaryMarketLongTermNoticeboardEntryResponse(BaseModel):
    """
    SecondaryMarketLongTermNoticeboardEntryResponse
    """
    reponse_capacity: StrictInt = Field(..., alias="reponseCapacity", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    response_price: Union[confloat(multiple_of=0.01, strict=True), conint(strict=True)] = Field(..., alias="responsePrice", description="Currency value in Euros (€), accepted with a precision of maximum 2 decimal places")
    contact_name: StrictStr = Field(..., alias="contactName")
    phone_number: constr(strict=True) = Field(..., alias="phoneNumber")
    email: constr(strict=True) = Field(...)
    comment: Optional[StrictStr] = None
    responded_at: datetime = Field(..., alias="respondedAt", description="Date and time with zone information, marks an **absolute point** on the timeline  - theoretically can be sent and received with any zone offset (until it marks the desired **absolute point** on the timeline) - in practice it is advised to transfer it in UTC timezone (with Z offset, \"Zulu time\") - ISO 8601 compliant string in `yyyy-mm-ddThh:mm:ss.SSSZ` format ")
    __properties = ["reponseCapacity", "responsePrice", "contactName", "phoneNumber", "email", "comment", "respondedAt"]

    # @validator('phone_number')
    def phone_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+\d{10,13}$", value):
            raise ValueError(r"must validate the regular expression /^\+\d{10,13}$/")
        return value

    # @validator('email')
    def email_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,6}$", value):
            raise ValueError(r"must validate the regular expression /^[\w-\.]+@([\w-]+\.)+[\w-]{2,6}$/")
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
    def from_json(cls, json_str: str) -> SecondaryMarketLongTermNoticeboardEntryResponse:
        """Create an instance of SecondaryMarketLongTermNoticeboardEntryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SecondaryMarketLongTermNoticeboardEntryResponse:
        """Create an instance of SecondaryMarketLongTermNoticeboardEntryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SecondaryMarketLongTermNoticeboardEntryResponse.parse_obj(obj)

        _obj = SecondaryMarketLongTermNoticeboardEntryResponse.parse_obj({
            "reponse_capacity": obj.get("reponseCapacity"),
            "response_price": obj.get("responsePrice"),
            "contact_name": obj.get("contactName"),
            "phone_number": obj.get("phoneNumber"),
            "email": obj.get("email"),
            "comment": obj.get("comment"),
            "responded_at": obj.get("respondedAt")
        })
        return _obj

