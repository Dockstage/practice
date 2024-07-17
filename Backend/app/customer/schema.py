from pydantic import BaseModel, Field


class SCustomer(BaseModel):
    customer_code: str
    customer_name: str
    customer_inn: str
    customer_kpp: str
    customer_legal_address: str
    customer_postal_address: str
    customer_email: str
    customer_code_main: str
    is_organization: bool
    is_person: bool

    class Config:
        from_attributes = True


class SCustomerResponse(BaseModel):
    Customer: SCustomer = Field()


class SPartialCustomer(BaseModel):
    customer_name: str | None = None
    customer_inn: str | None = None
    customer_kpp: str | None = None
    customer_legal_address: str | None = None
    customer_postal_address: str | None = None
    customer_email: str | None = None
    customer_code_main: str | None = None
    is_organization: bool | None = None
    is_person: bool | None = None

    class Config:
        from_attributes = True
