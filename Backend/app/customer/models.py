from sqlalchemy import Column, Boolean, String

from app.database import Base


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {'schema': 'purchase'}

    customer_code = Column(String, primary_key=True)
    customer_name = Column(String, nullable=False)
    customer_inn = Column(String, nullable=False)
    customer_kpp = Column(String, nullable=False)
    customer_legal_address = Column(String)
    customer_postal_address = Column(String)
    customer_email = Column(String)
    customer_code_main = Column(String)
    is_organization = Column(Boolean, nullable=False)
    is_person = Column(Boolean, nullable=False)
