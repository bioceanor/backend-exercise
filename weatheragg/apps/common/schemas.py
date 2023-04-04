from datetime import datetime
from enum import Enum
from typing import List, Optional

from apps.common.models import DataPointModel
from ninja import FilterSchema, ModelSchema, Schema


class Aggregation(str, Enum):
    AVG = "avg"
    MIN = "min"
    MAX = "max"


class QueryFilterSchema(FilterSchema):
    start: datetime
    end: Optional[datetime]
    location_id: int
    agg_interval: Optional[int]
    agg: Optional[Aggregation]


class DataPoint(ModelSchema):
    class Config:
        model = DataPointModel
        model_exclude = ["id", "param"]


class DataAPIResponse(Schema):
    data: List[DataPoint]
