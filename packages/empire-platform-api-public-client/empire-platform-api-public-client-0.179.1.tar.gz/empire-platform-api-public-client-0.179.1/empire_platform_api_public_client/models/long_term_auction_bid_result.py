# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.179.1
    Contact: britned.info@britned.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from empire_platform_api_public_client.models.auction_bid_participant import AuctionBidParticipant
from empire_platform_api_public_client.models.auction_bid_status import AuctionBidStatus
from empire_platform_api_public_client.models.bid_value import BidValue

class LongTermAuctionBidResult(BaseModel):
    """
    LongTermAuctionBidResult
    """
    id: Optional[StrictStr] = Field(None, description="Unique identifier for the record in UUID4 format")
    participant: Optional[AuctionBidParticipant] = None
    value: BidValue = Field(...)
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="Date and time with zone information, marks an **absolute point** on the timeline  - theoretically can be sent and received with any zone offset (until it marks the desired **absolute point** on the timeline) - in practice it is advised to transfer it in UTC timezone (with Z offset, \"Zulu time\") - ISO 8601 compliant string in `yyyy-mm-ddThh:mm:ss.SSSZ` format ")
    status: AuctionBidStatus = Field(...)
    __properties = ["id", "participant", "value", "updatedAt", "status"]

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
    def from_json(cls, json_str: str) -> LongTermAuctionBidResult:
        """Create an instance of LongTermAuctionBidResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of participant
        if self.participant:
            _dict['participant'] = self.participant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LongTermAuctionBidResult:
        """Create an instance of LongTermAuctionBidResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LongTermAuctionBidResult.parse_obj(obj)

        _obj = LongTermAuctionBidResult.parse_obj({
            "id": obj.get("id"),
            "participant": AuctionBidParticipant.from_dict(obj.get("participant")) if obj.get("participant") is not None else None,
            "value": BidValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "updated_at": obj.get("updatedAt"),
            "status": obj.get("status")
        })
        return _obj

