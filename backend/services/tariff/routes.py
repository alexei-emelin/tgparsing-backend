from fastapi import APIRouter, Depends

from services.tariff import views
from services.tariff.schemas import TariffLimitResponse, TariffResponse
from services.user.utils.permissions import is_superuser

# from services.user.utils.permissions import is_superuser
from settings import config

tariff_router = APIRouter(prefix="/tariff", tags=["Tariff"])

tariff_router.add_api_route(
    path="/",
    endpoint=views.get_tariff_list_view,
    methods=["GET"],
    name=config.TARIFF_GET_ALL,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/",
    endpoint=views.create_tariff_view,
    methods=["POST"],
    name=config.TARIFF_ADD,
    response_model=TariffResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/{tariff_id}",
    endpoint=views.get_tariff_view,
    methods=["GET"],
    name=config.TARIFF_GET,
    response_model=TariffResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/{tariff_id}",
    endpoint=views.change_tariff_view,
    methods=["PATCH"],
    name=config.TARIFF_PATCH,
    response_model=TariffResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/{tariff_id}",
    endpoint=views.delete_tariff_view,
    methods=["DELETE"],
    name=config.TARIFF_DELETE,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices",
    endpoint=views.tariff_prices_list_view,
    methods=["GET"],
    name=config.TARIFF_PRICE_GET_ALL,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices/{tariff_price_id}",
    endpoint=views.get_tariff_price_view,
    methods=["GET"],
    name=config.TARIFF_PRICE_GET,
    response_model=TariffLimitResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices",
    endpoint=views.create_tariff_price_view,
    methods=["POST"],
    name=config.TARIFF_PRICE_ADD,
    response_model=TariffLimitResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices/{tariff_price_id}",
    endpoint=views.change_tariff_price_view,
    methods=["PATCH"],
    name=config.TARIFF_PRICE_PATCH,
    response_model=TariffLimitResponse,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices/{tariff_price_id}",
    endpoint=views.delete_tariff_price_view,
    methods=["DELETE"],
    name=config.TARIFF_PRICE_DELETE,
    dependencies=[Depends(is_superuser)],
)

tariff_router.add_api_route(
    path="/limit/prices/all/{tariff_id}",
    endpoint=views.get_tariff_prices_view,
    methods=["GET"],
    name=config.TARIFF_PRICES_GET,
    dependencies=[Depends(is_superuser)],
)