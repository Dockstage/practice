from sqlalchemy import Column, String, ForeignKey, Numeric, TIMESTAMP

from app.database import Base


class Lot(Base):
    __tablename__ = "lot"
    __table_args__ = {'schema': 'purchase'}

    lot_name = Column(String, primary_key=True,  nullable=False)
    customer_code = Column(String, ForeignKey('purchase.customer.customer_code'), nullable=False)
    price = Column(Numeric, nullable=False)
    currency_code = Column(String, nullable=False)
    nds_rate = Column(String, nullable=False)
    place_delivery = Column(String, nullable=False)
    date_delivery = Column(TIMESTAMP, nullable=False)
