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


from typing import List
from pydantic import BaseModel, Field, conlist, constr
from vrt_lss_universal.models.statistics import Statistics
from vrt_lss_universal.models.stop_statistics import StopStatistics
from vrt_lss_universal.models.transport_load import TransportLoad

class TripStatistics(BaseModel):
    """
    Statistics for a specific trip. 
    """
    trip_key: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="Trip key, unique identifier")
    statistics: Statistics = Field(...)
    stop_statistics: conlist(StopStatistics, max_items=15001, min_items=0) = Field(..., description="Statistics per stop during the trip.")
    total_load: TransportLoad = Field(...)
    max_load: TransportLoad = Field(...)
    max_transfer_load: TransportLoad = Field(...)
    __properties = ["trip_key", "statistics", "stop_statistics", "total_load", "max_load", "max_transfer_load"]

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
    def from_json(cls, json_str: str) -> TripStatistics:
        """Create an instance of TripStatistics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stop_statistics (list)
        _items = []
        if self.stop_statistics:
            for _item in self.stop_statistics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stop_statistics'] = _items
        # override the default output from pydantic by calling `to_dict()` of total_load
        if self.total_load:
            _dict['total_load'] = self.total_load.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_load
        if self.max_load:
            _dict['max_load'] = self.max_load.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_transfer_load
        if self.max_transfer_load:
            _dict['max_transfer_load'] = self.max_transfer_load.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TripStatistics:
        """Create an instance of TripStatistics from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TripStatistics.parse_obj(obj)

        _obj = TripStatistics.parse_obj({
            "trip_key": obj.get("trip_key"),
            "statistics": Statistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "stop_statistics": [StopStatistics.from_dict(_item) for _item in obj.get("stop_statistics")] if obj.get("stop_statistics") is not None else None,
            "total_load": TransportLoad.from_dict(obj.get("total_load")) if obj.get("total_load") is not None else None,
            "max_load": TransportLoad.from_dict(obj.get("max_load")) if obj.get("max_load") is not None else None,
            "max_transfer_load": TransportLoad.from_dict(obj.get("max_transfer_load")) if obj.get("max_transfer_load") is not None else None
        })
        return _obj

