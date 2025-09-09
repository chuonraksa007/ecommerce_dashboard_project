import pytest
import httpx
from app.base.untility import settings

@pytest.mark.asyncio
async def test_ecom_dashboard():
    async with httpx.AsyncClient(base_url=settings.TEST_BASE_URL) as client:
        resp = await client.get("/ecoms/dashboard")
        assert resp.status_code == 200