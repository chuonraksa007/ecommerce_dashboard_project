from pydantic_settings import BaseSettings
from datetime import datetime
import pytz
from typing import Any, List, Optional, Dict, Tuple
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar
from pydantic import BaseModel
from sqlalchemy.sql import text
from datetime import datetime
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

T = TypeVar("T")

class AppSuccessResponse(BaseModel, Generic[T]):
    code: int = 200
    msg: str = "Success"
    data: T
    """    A generic class for success responses.
    Attributes:
        code: HTTP status code (default 200)
        msg: Response message
        data: Response data
    """

async def paginate(
    db: AsyncSession,
    model: Any,
    filters: List[Any],
    page: int = 1,
    page_size: int = 10
) -> Tuple[List[Any], int, int]:
    """
    Reusable pagination function.

    Args:
        db: AsyncSession model
        model: SQLAlchemy ORM model class
        filters: List of filter expressions
        page: Current page number (1-based)
        page_size: Number of items per page

    Returns:
        Tuple containing:
            - List of model models for the current page
            - Total number of matching records
            - Total number of pages
    """
    count_query = select(func.count()).select_from(model).where(*filters)
    total_records_result = await db.execute(count_query)
    total_records = total_records_result.scalar_one()
    offset = (page - 1) * page_size
    query = select(model).where(*filters).offset(offset).limit(page_size)
    result = await db.execute(query)
    items = result.scalars().all()
    total_pages = (total_records + page_size - 1) // page_size
    return items, total_records, total_pages

def app_success_paginated(
    data: Optional[Any] = None,
    msg: Optional[str]= None,
    code: int = 200,
    total_records: Optional[int] = None,
    total_pages: Optional[int] = None,
    current_page: Optional[int] = None,
    page_size: Optional[int] = None,
    lists: Optional[List[Dict]] = None,
    extra: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Standardized success response formatter.

    Supports paginated response if pagination params are provided.

    Args:
        data: Arbitrary response data for non-paginated response
        msg: Response message
        code: HTTP status code (default 200)
        total_records: Total number of records (for paginated)
        total_pages: Total pages count (for paginated)
        current_page: Current page number (for paginated)
        page_size: Page size (for paginated)
        lists: List of items (for paginated)

    Returns:
        Dict formatted response ready to return as JSON.
    """
    if msg is None:
        msg = "Success"
    response = {
        "code": code,
        "msg": msg,
    }
    if all(v is not None for v in [total_records, total_pages, current_page, page_size, lists]):
        base_data = {
            "total_records": total_records,
            "total_pages": total_pages,
            "current_page": current_page,
            "page_size": page_size,
        }
        if extra:
            base_data.update(extra)  
        base_data["lists"] = lists 
        response["data"] = base_data
    else:
        response["data"] = data
    return response

def app_success(
    msg: Optional[str] = None,
    code: int = 200,
    data: Optional[Any] = None,
):
    """
    Standardized success response formatter.

    Args:
        msg: Success message
        code: HTTP status code (default 200)
        data: Optional returned data

    Returns:
        Dict formatted success response
    """
    if msg is None:
        msg = "success"
    return {
        "code": code,
        "msg": msg,
        "data": data
    }

def app_error(
    msg: Optional[str] = None,
    code: int = 400,
    data: Optional[Any] = None,
):
    """
    Standardized error response formatter.

    Args:
        msg: Error message
        code: HTTP status code (default 400)
        data: Optional returned data

    Returns:
        Dict formatted error response
    """
    if msg is None:
        msg = "fail"
    return {
        "code": code,
        "msg": msg,
        "data": data
    }

def app_server_error(
    msg: Optional[str] = None,
    code: int = 500,
    data: Optional[Any] = None,
):
    """
    Standardized server error response formatter.

    Args:
        msg: Error message
        code: HTTP status code (default 500)
        data: Optional returned data

    Returns:
        Dict formatted error response
    """
    if msg is None:
        msg = "server_error"
    return {
        "code": code,
        "msg": msg,
        "data": data
    }

def get_phnom_penh_time():
    """
    get date time in phnom penh 
    """
    phnom_penh_tz = pytz.timezone('Asia/Phnom_Penh')
    dt = datetime.now(phnom_penh_tz)
    return dt.replace(tzinfo=None)

class AppException(HTTPException):
    def __init__(self, code: int, msg: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail={
            "code": code,
            "msg": msg,
            "data": None
        })

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_BASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
    