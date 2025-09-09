from sqlalchemy import Column, Integer, String, DateTime, Float, Index
from app.base.database import Base

class Product(Base):
    __tablename__ = "ecom_product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    qty = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        Index('idx_product_category_id', 'category_id'),
    )
