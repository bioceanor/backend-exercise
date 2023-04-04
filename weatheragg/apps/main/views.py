from typing import List

from apps.main.schemas import LocationSchemaIn, LocationSchemaOut
from ninja import Router

router = Router()


@router.post("/location", url_name="Create Location")
def create_location(request, data: LocationSchemaIn):
    ...


@router.get(
    "/location/{location_id}",
    url_name="Get a Location",
    response=LocationSchemaOut,
)
def get_location(request, location_id: int) -> LocationSchemaOut:
    ...


@router.get(
    "/location", url_name="List All Locations", response=List[LocationSchemaOut]
)
def list_locations(request) -> List[LocationSchemaOut]:
    ...


@router.delete(
    "location/{location_id}", url_name="Delete Location", response=LocationSchemaOut
)
def delete_location(request, location_id: int) -> LocationSchemaOut:
    ...
