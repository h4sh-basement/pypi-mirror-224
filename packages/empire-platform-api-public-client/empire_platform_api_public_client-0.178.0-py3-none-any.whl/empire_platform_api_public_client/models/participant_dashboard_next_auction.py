# coding: utf-8

"""
    Empire - Platform API

    OpenAPI specification for the Platform REST API of Empire  **System Time:** Europe/Amsterdam  **General data formats:**   * _capacity values_ => kW (integers)   * _dates and local times_ => System Time   * _currencies_ => EUR   # noqa: E501

    The version of the OpenAPI document: 0.178.0
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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint
from empire_platform_api_public_client.models.auction_product_type import AuctionProductType
from empire_platform_api_public_client.models.auction_status import AuctionStatus
from empire_platform_api_public_client.models.border_direction import BorderDirection
from empire_platform_api_public_client.models.mtu_period import MtuPeriod

class ParticipantDashboardNextAuction(BaseModel):
    """
    * `offeredCapacity` = Offered capacity in kilowatts. Optional, only set for LT auctions, and should be calculated as MAX(OC) over the MTUs in the delivery period. 
    """
    id: StrictStr = Field(..., description="Unique identifier for the record in UUID4 format")
    name: StrictStr = Field(..., description="Human readable name")
    delivery_period: MtuPeriod = Field(..., alias="deliveryPeriod")
    product_type: AuctionProductType = Field(..., alias="productType")
    border_direction: BorderDirection = Field(..., alias="borderDirection")
    status: AuctionStatus = Field(...)
    pre_bidding_allowed: StrictBool = Field(..., alias="preBiddingAllowed")
    bids_count: conint(strict=True, ge=0) = Field(..., alias="bidsCount", description="Natural numbers {0, 1, 2, 3, ...} used for counting elements")
    offered_capacity: Optional[StrictInt] = Field(None, alias="offeredCapacity", description="Capacity value in kilowatts (kW) - the required system precision allows for handling capacity values as integers")
    next_action_at: Optional[datetime] = Field(None, alias="nextActionAt", description="Date and time with zone information, marks an **absolute point** on the timeline  - theoretically can be sent and received with any zone offset (until it marks the desired **absolute point** on the timeline) - in practice it is advised to transfer it in UTC timezone (with Z offset, \"Zulu time\") - ISO 8601 compliant string in `yyyy-mm-ddThh:mm:ss.SSSZ` format ")
    __properties = ["id", "name", "deliveryPeriod", "productType", "borderDirection", "status", "preBiddingAllowed", "bidsCount", "offeredCapacity", "nextActionAt"]

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
    def from_json(cls, json_str: str) -> ParticipantDashboardNextAuction:
        """Create an instance of ParticipantDashboardNextAuction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of delivery_period
        if self.delivery_period:
            _dict['deliveryPeriod'] = self.delivery_period.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParticipantDashboardNextAuction:
        """Create an instance of ParticipantDashboardNextAuction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParticipantDashboardNextAuction.parse_obj(obj)

        _obj = ParticipantDashboardNextAuction.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "delivery_period": MtuPeriod.from_dict(obj.get("deliveryPeriod")) if obj.get("deliveryPeriod") is not None else None,
            "product_type": obj.get("productType"),
            "border_direction": obj.get("borderDirection"),
            "status": obj.get("status"),
            "pre_bidding_allowed": obj.get("preBiddingAllowed"),
            "bids_count": obj.get("bidsCount"),
            "offered_capacity": obj.get("offeredCapacity"),
            "next_action_at": obj.get("nextActionAt")
        })
        return _obj

