from typing import List
from pydantic import BaseModel


class Filter(BaseModel):
    value: str
    propertyName: str
    operator: str


class FilterGroup(BaseModel):
    filters: List[Filter]


class ContactSearchRequest(BaseModel):
    filterGroups: List[FilterGroup]
    limit: int = 100
