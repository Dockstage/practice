from fastapi import FastAPI

from app.customer.router import router_customer
from app.lot.router import router_lot

app = FastAPI()

app.include_router(router_customer)
app.include_router(router_lot)