from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.lot.service import LotService
from app.lot.schema import SLot, SLotResponse, SPartialLot
from typing import List

router_lot = APIRouter(prefix="/lot", tags=["lot"])


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


@router_lot.post("/", response_model=SLotResponse)
async def create_lot(lot: SLot, session: AsyncSession = Depends(get_session)):
    service = LotService(session)
    result = await service.create(lot)
    return SLotResponse(Lot=result)


@router_lot.get("/{lot_name}", response_model=SLotResponse)
async def read_lot(lot_name: str, session: AsyncSession = Depends(get_session)):
    service = LotService(session)
    result = await service.read(lot_name)
    if not result:
        raise HTTPException(status_code=404, detail="Lot not found")
    return SLotResponse(Lot=result)


@router_lot.get("/", response_model=List[SLot])
async def read_all_lots(session: AsyncSession = Depends(get_session)):
    service = LotService(session)
    result = await service.read_all()
    return result


@router_lot.patch("/{lot_name}", response_model=SLotResponse)
async def update_lot(lot_name: str, lot: SPartialLot, session: AsyncSession = Depends(get_session)):
    service = LotService(session)
    result = await service.update(lot_name, lot)
    if not result:
        raise HTTPException(status_code=404, detail="Lot not found")
    return SLotResponse(Lot=result)


@router_lot.delete("/{lot_name}", response_model=SLotResponse)
async def delete_lot(lot_name: str, session: AsyncSession = Depends(get_session)):
    service = LotService(session)
    result = await service.delete(lot_name)
    if not result:
        raise HTTPException(status_code=404, detail="Lot not found")
    return SLotResponse(Lot=result)
