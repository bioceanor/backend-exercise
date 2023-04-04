from apps.common.schemas import DataAPIResponse, QueryFilterSchema
from ninja import Query, Router

router = Router()


@router.get("/temperature", url_name="Air Temperature", response=DataAPIResponse)
def get_air_temperature(
    request, filters: QueryFilterSchema = Query(...)
) -> DataAPIResponse:
    ...


@router.get("/humidity", url_name="Air Humidity", response=DataAPIResponse)
def get_air_humidity(
    request, filters: QueryFilterSchema = Query(...)
) -> DataAPIResponse:
    ...
