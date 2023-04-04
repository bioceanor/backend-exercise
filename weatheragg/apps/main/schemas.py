from apps.main.models import LocationModel
from ninja import ModelSchema


class LocationSchemaOut(ModelSchema):
    class Config:
        model = LocationModel
        model_fields = "__all__"


class LocationSchemaIn(ModelSchema):
    class Config:
        model = LocationModel
        model_exclude = ["id"]
