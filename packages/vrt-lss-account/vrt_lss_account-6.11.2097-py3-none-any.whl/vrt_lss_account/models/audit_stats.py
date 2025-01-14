# coding: utf-8

"""
    VRt.Account [AC]

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



from pydantic import BaseModel, Field
from vrt_lss_account.models.audit_stats_detail import AuditStatsDetail

class AuditStats(BaseModel):
    """
    Statistics by records list.
    """
    overall: AuditStatsDetail = Field(...)
    filter: AuditStatsDetail = Field(...)
    __properties = ["overall", "filter"]

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
    def from_json(cls, json_str: str) -> AuditStats:
        """Create an instance of AuditStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of overall
        if self.overall:
            _dict['overall'] = self.overall.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditStats:
        """Create an instance of AuditStats from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AuditStats.parse_obj(obj)

        _obj = AuditStats.parse_obj({
            "overall": AuditStatsDetail.from_dict(obj.get("overall")) if obj.get("overall") is not None else None,
            "filter": AuditStatsDetail.from_dict(obj.get("filter")) if obj.get("filter") is not None else None
        })
        return _obj

