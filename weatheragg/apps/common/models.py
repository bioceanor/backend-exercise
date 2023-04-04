from django.db import models

WEATHER_PARAMS = [
    ("WT", "WaterTemperature"),
    ("AT", "AirTemperature"),
    ("AH", "AirHumidity"),
    ("DO", "DissolvedOxygen"),
]


class DataPointModel(models.Model):
    value = models.FloatField()
    ts = models.DateTimeField()
    param = models.CharField(max_length=2, choices=WEATHER_PARAMS)
