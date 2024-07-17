from app.lot.models import Lot
from app.service.base import BaseService


class LotService(BaseService):
    model = Lot
