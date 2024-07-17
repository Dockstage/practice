from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime


class SLot(BaseModel):
    lot_name: str
    customer_code: str
    price: Decimal
    currency_code: str
    nds_rate: str
    place_delivery: str
    date_delivery: datetime

    class Config:
        from_attributes = True


class SLotResponse(BaseModel):
    Lot: SLot = Field()


class SPartialLot(BaseModel):
    customer_code: str | None = None
    price: Decimal | None = None
    currency_code: str | None = None
    nds_rate: str | None = None
    place_delivery: str | None = None
    date_delivery: datetime | None = None

    class Config:
        from_attributes = True
