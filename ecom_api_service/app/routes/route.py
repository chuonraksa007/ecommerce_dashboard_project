from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.base.database import get_db
from typing import Optional, Union
from app.controller.ecom_controller import index_ecom
from app.schemas.order_schema import OrderData
from app.schemas.order_schema import Order as OrderSchema
from app.base.untility import AppSuccessResponse

router = APIRouter()

@router.get("/ecoms/dashboard", response_model=Union[AppSuccessResponse[OrderSchema], dict])
async def func_index_ecom(
    db: AsyncSession = Depends(get_db)
):
    return await index_ecom(db)
                                                                                                                                                                                                                                                                                                                                                                                                                                                             