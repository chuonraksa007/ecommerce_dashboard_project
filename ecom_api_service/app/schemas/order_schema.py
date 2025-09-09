from fastapi import Form
from pydantic import BaseModel, ConfigDict
from typing import  Optional

class OrderBase(BaseModel):
       customer_id: Optional[str] = None
       product_id: Optional[str] = None
       category_id: Optional[str] = None
       qty: Optional[int] = None
       amount: Optional[float] = None
       status: Optional[str] = None
       created_at: Optional[str] = None
       updated_at: Optional[str] = None
       qty:Optional[int]=None,
       amount:Optional[float]=None,
       model_config = ConfigDict(from_attributes=True)

class OrderData(OrderBase):
      @staticmethod
      def as_form(
            customer_id: Optional[str] = Form(None),
            product_id: Optional[str] = Form(None),
            category_id: Optional[str] = Form(None),
            qty: Optional[int] = Form(None),
            amount: Optional[float] = Form(None),
            status: Optional[str] = Form(None),
            created_at: Optional[str] = Form(None),
            updated_at: Optional[str] = Form(None),
      ):
            return OrderData(
            customer_id=customer_id,
            product_id=product_id,
            category_id=category_id,
            qty=qty,
            amount=amount,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
      )
class Order(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
    