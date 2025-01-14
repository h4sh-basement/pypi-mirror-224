# coding: utf-8

"""
    VRt.Studio [ST]

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
from vrt_lss_studio.models.trip import Trip
from vrt_lss_studio.models.web_trip_chart_demand import WebTripChartDemand

class WebTripChart(BaseModel):
    """
    Trip for chart.
    """
    trip: Trip = Field(...)
    chart_demands: conlist(WebTripChartDemand, max_items=15001, min_items=0) = Field(..., description="A list of demands info.")
    __properties = ["trip", "chart_demands"]

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
    def from_json(cls, json_str: str) -> WebTripChart:
        """Create an instance of WebTripChart from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trip
        if self.trip:
            _dict['trip'] = self.trip.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in chart_demands (list)
        _items = []
        if self.chart_demands:
            for _item in self.chart_demands:
                if _item:
                    _items.append(_item.to_dict())
            _dict['chart_demands'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebTripChart:
        """Create an instance of WebTripChart from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WebTripChart.parse_obj(obj)

        _obj = WebTripChart.parse_obj({
            "trip": Trip.from_dict(obj.get("trip")) if obj.get("trip") is not None else None,
            "chart_demands": [WebTripChartDemand.from_dict(_item) for _item in obj.get("chart_demands")] if obj.get("chart_demands") is not None else None
        })
        return _obj

