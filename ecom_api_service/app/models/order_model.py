from sqlalchemy import CHAR, Column, Integer, String, Index, ForeignKey
from app.base.database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Order(Base):
    __tablename__ = "ecom_order"
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer(), nullable=False)
    product_id = Column(Integer(), nullable=False)
    category_id = Column(Integer(), nullable=False)
    qty = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, default='pending')
    created_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    __table_args__ = (
        Index('idx_product_id', 'product_id'),
        Index('idx_category_id', 'category_id'),
        Index('idx_customer_id', 'customer_id'),
    )