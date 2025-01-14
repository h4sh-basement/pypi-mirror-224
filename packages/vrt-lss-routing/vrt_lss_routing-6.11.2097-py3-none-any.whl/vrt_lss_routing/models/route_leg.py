# coding: utf-8

"""
    VRt.Routing [RO]

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
from pydantic import BaseModel, Field, conlist
from vrt_lss_routing.models.route_statistics import RouteStatistics
from vrt_lss_routing.models.route_step import RouteStep

class RouteLeg(BaseModel):
    """
    The route leg between two locations.
    """
    steps: conlist(RouteStep, max_items=10, min_items=0) = Field(..., description="Steps required to pass a route leg.")
    statistics: RouteStatistics = Field(...)
    __properties = ["steps", "statistics"]

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
    def from_json(cls, json_str: str) -> RouteLeg:
        """Create an instance of RouteLeg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RouteLeg:
        """Create an instance of RouteLeg from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RouteLeg.parse_obj(obj)

        _obj = RouteLeg.parse_obj({
            "steps": [RouteStep.from_dict(_item) for _item in obj.get("steps")] if obj.get("steps") is not None else None,
            "statistics": RouteStatistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None
        })
        return _obj

