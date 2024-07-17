from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.customer.service import CustomerService
from app.customer.schema import SCustomer, SCustomerResponse, SPartialCustomer
from typing import List

router_customer = APIRouter(prefix="/customer", tags=["customer"])


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


@router_customer.post("/", response_model=SCustomerResponse)
async def create_customer(customer: SCustomer, session: AsyncSession = Depends(get_session)):
    service = CustomerService(session)
    result = await service.create(customer)
    return SCustomerResponse(Customer=result)


@router_customer.get("/{customer_code}", response_model=SCustomerResponse)
async def read_customer(customer_code: str, session: AsyncSession = Depends(get_session)):
    service = CustomerService(session)
    result = await service.read(customer_code)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return SCustomerResponse(Customer=result)


@router_customer.get("/", response_model=List[SCustomer])
async def read_all_customers(session: AsyncSession = Depends(get_session)):
    service = CustomerService(session)
    result = await service.read_all()
    return result


@router_customer.patch("/{customer_code}", response_model=SCustomerResponse)
async def update_customer(customer_code: str, customer: SPartialCustomer, session: AsyncSession = Depends(get_session)):
    service = CustomerService(session)
    result = await service.update(customer_code, customer)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return SCustomerResponse(Customer=result)


@router_customer.delete("/{customer_code}", response_model=SCustomerResponse)
async def delete_customer(customer_code: str, session: AsyncSession = Depends(get_session)):
    service = CustomerService(session)
    result = await service.delete(customer_code)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return SCustomerResponse(Customer=result)
