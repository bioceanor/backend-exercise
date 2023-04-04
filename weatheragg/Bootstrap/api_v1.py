from apps.air.views import router as air_router
from apps.main.views import router as main_router
from apps.water.views import router as water_router
from ninja import NinjaAPI

api_v1 = NinjaAPI(title="Weather Agg APIs", version="1")
api_v1.add_router("/main/", main_router, tags=["Main"])
api_v1.add_router("/air/", air_router, tags=["Air"])
api_v1.add_router("/water/", water_router, tags=["Water"])
