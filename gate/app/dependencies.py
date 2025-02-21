from httpx import AsyncClient

async def get_http_client() -> AsyncClient:
  return AsyncClient(timeout=10.0)