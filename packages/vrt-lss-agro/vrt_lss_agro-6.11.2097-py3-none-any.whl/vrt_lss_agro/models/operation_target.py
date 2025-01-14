# coding: utf-8

"""
    VRt.Agro [AG]

    The version of the OpenAPI document: 6.11.2097

    Generated by OpenAPI Generator: 6.6.0

    Do not edit the code manually

    2023 Veeroute
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel, Field, confloat, conint, conlist, constr
from vrt_lss_agro.models.attribute import Attribute
from vrt_lss_agro.models.crop_type import CropType
from vrt_lss_agro.models.object_type import ObjectType

class OperationTarget(BaseModel):
    """
    Operation target. 
    """
    var_date: date = Field(..., alias="date", description="Date in the YYYY-MM-DD format.")
    target_key: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="Target key.")
    target_type: ObjectType = Field(...)
    target_detail_key: Optional[constr(strict=True, max_length=1024, min_length=1)] = Field(None, description="The key of the object part, if it exists for this operation - [more](#section/Description/Project). ")
    crop_type: CropType = Field(...)
    humidity: conint(strict=True, le=999, ge=1) = Field(..., description="Humidity crop, in ppm (‰).")
    mass: Union[confloat(le=10000000.1, ge=0, strict=True), conint(le=10000000, ge=0, strict=True)] = Field(..., description="Weight, in tn.")
    attributes: Optional[conlist(Attribute, max_items=1000, min_items=0, unique_items=True)] = Field(None, description="Attributes. Used to add service information.")
    __properties = ["date", "target_key", "target_type", "target_detail_key", "crop_type", "humidity", "mass", "attributes"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OperationTarget:
        """Create an instance of OperationTarget from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # set to None if target_detail_key (nullable) is None
        # and __fields_set__ contains the field
        if self.target_detail_key is None and "target_detail_key" in self.__fields_set__:
            _dict['target_detail_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OperationTarget:
        """Create an instance of OperationTarget from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OperationTarget.parse_obj(obj)

        _obj = OperationTarget.parse_obj({
            "var_date": obj.get("date"),
            "target_key": obj.get("target_key"),
            "target_type": obj.get("target_type"),
            "target_detail_key": obj.get("target_detail_key"),
            "crop_type": obj.get("crop_type"),
            "humidity": obj.get("humidity"),
            "mass": obj.get("mass"),
            "attributes": [Attribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None
        })
        return _obj

