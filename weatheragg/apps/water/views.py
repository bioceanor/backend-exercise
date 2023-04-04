from apps.common.schemas import DataAPIResponse, QueryFilterSchema
from ninja import Query, Router

router = Router()


@router.get("/temperature", url_name="Water Temperature", response=DataAPIResponse)
def get_water_temperature(
    request, filters: QueryFilterSchema = Query(...)
) -> DataAPIResponse:
    ...


@router.get(
    "/dissolved-oxygen", url_name="Water Dissolved Oxugen", response=DataAPIResponse
)
def get_dissolved_oxygen(
    request, filters: QueryFilterSchema = Query(...)
) -> DataAPIResponse:
    ...
