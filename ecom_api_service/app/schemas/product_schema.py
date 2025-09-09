from fastapi import Form
from pydantic import BaseModel, ConfigDict
from typing import  Optional

class productBase(BaseModel):
       name: Optional[str] = None
       qty: Optional[int] = None
       amount: Optional[float] = None
       category_id: Optional[str] = None
       created_at: Optional[str] = None
       updated_at: Optional[str] = None
       qty:Optional[int]=None,
       amount:Optional[float]=None,
       model_config = ConfigDict(from_attributes=True)

class productData(productBase):
      @staticmethod
      def as_form(
            name: Optional[str] = Form(None),
            qty: Optional[int] = Form(None),
            amount: Optional[float] = Form(None),
            category_id: Optional[str] = Form(None),
            created_at: Optional[str] = Form(None),
            updated_at: Optional[str] = Form(None),
      ):
            return productData(
            name=name,
            qty=qty,
            amount=amount,
            category_id=category_id,
            created_at=created_at,
            updated_at=updated_at,
      )

class OrderBase(BaseModel):
       customer_id: Optional[str] = None
       product_id: Optional[str] = None
       category_id: Optional[str] = None
       qty: Optional[int] = None
       amount: Optional[float] = None
       created_at: Optional[str] = None
       updated_at: Optional[str] = None
       qty:Optional[int]=None,
       amount:Optional[float]=None,
       model_config = ConfigDict(from_attributes=True)

class Product(productBase):
    id: int
    model_config = ConfigDict(from_attributes=True)