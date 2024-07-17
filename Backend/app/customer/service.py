from app.customer.models import Customer
from app.service.base import BaseService


class CustomerService(BaseService):
    model = Customer
