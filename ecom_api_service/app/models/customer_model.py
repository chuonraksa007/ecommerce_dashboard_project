from sqlalchemy import CHAR, Column, Integer, String, Index, ForeignKey
from app.base.database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Customer(Base):
    __tablename__ = "ecom_customer"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    __table_args__ = (
        Index('idx_customer_name', 'name'),
    )