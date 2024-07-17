# app/service/base.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound


class BaseService:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, obj_in):
        obj = self.model(**obj_in.dict())
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def read(self, obj_id):
        stmt = select(self.model).where(self.model.customer_code == obj_id)
        result = await self.session.execute(stmt)
        try:
            return result.scalars().one()
        except NoResultFound:
            return None

    async def read_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update(self, obj_id, obj_in):
        obj = await self.read(obj_id)
        if not obj:
            return None
        for key, value in obj_in.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, obj_id):
        obj = await self.read(obj_id)
        if not obj:
            return None
        await self.session.delete(obj)
        await self.session.commit()
        return obj
