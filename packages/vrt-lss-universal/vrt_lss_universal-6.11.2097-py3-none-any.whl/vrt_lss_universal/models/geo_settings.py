# coding: utf-8

"""
    VRt.Universal [UV]

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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist, constr

class GeoSettings(BaseModel):
    """
    Geodata usage settings. 
    """
    geo_provider: Optional[constr(strict=True, max_length=256, min_length=1)] = Field('OSRM', description="Geodata provider.")
    toll_roads: Optional[StrictBool] = Field(True, description="Use toll roads.")
    ferry_crossing: Optional[StrictBool] = Field(True, description="Use ferry crossing.")
    traffic_jams: Optional[StrictBool] = Field(True, description="Accounting for traffic during the route planning.")
    flight_distance: Optional[StrictBool] = Field(False, description="Use for calculating straight line distances. If `false` is specified, distances are calculated by roads. When this parameter is enabled, geo-provider not used and traffic (`traffic_jams`) is automatically disabled. ")
    restricted_zones: Optional[conlist(constr(strict=True, max_length=256, min_length=1), max_items=5, min_items=0, unique_items=True)] = Field(None, description="List of restricted zones. ")
    __properties = ["geo_provider", "toll_roads", "ferry_crossing", "traffic_jams", "flight_distance", "restricted_zones"]

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
    def from_json(cls, json_str: str) -> GeoSettings:
        """Create an instance of GeoSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeoSettings:
        """Create an instance of GeoSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GeoSettings.parse_obj(obj)

        _obj = GeoSettings.parse_obj({
            "geo_provider": obj.get("geo_provider") if obj.get("geo_provider") is not None else 'OSRM',
            "toll_roads": obj.get("toll_roads") if obj.get("toll_roads") is not None else True,
            "ferry_crossing": obj.get("ferry_crossing") if obj.get("ferry_crossing") is not None else True,
            "traffic_jams": obj.get("traffic_jams") if obj.get("traffic_jams") is not None else True,
            "flight_distance": obj.get("flight_distance") if obj.get("flight_distance") is not None else False,
            "restricted_zones": obj.get("restricted_zones")
        })
        return _obj

