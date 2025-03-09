from typing import Any, Dict, Optional
import httpx
from pydantic import BaseModel

class QaseClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Token": token,
                "Content-Type": "application/json",
            },
        )

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        response = await self.client.request(
            method,
            path,
            params=params,
            json=json,
        )
        response.raise_for_status()
        return response.json()

    async def get_projects(self) -> Dict[str, Any]:
        """Get all projects"""
        return await self._request("GET", "/v1/project")

    async def get_test_cases(self, project_code: str) -> Dict[str, Any]:
        """Get all test cases for a project"""
        return await self._request("GET", f"/v1/case/{project_code}")

    async def create_test_case(
        self, project_code: str, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Create a new test case"""
        return await self._request("POST", f"/v1/case/{project_code}", json=data)

    async def get_test_runs(self, project_code: str) -> Dict[str, Any]:
        """Get all test runs for a project"""
        return await self._request("GET", f"/v1/run/{project_code}")

    async def create_test_run(
        self, project_code: str, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Create a new test run"""
        return await self._request("POST", f"/v1/run/{project_code}", json=data)

    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose() 