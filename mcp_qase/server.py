from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from .client import QaseClient

def create_app(base_url: str, token: str) -> FastAPI:
    app = FastAPI(title="MCP Qase API Server")
    
    # CORSミドルウェアの設定
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # QaseClientのインスタンスを作成
    client = QaseClient(base_url, token)

    @app.on_event("shutdown")
    async def shutdown_event():
        await client.close()

    @app.get("/api/projects")
    async def get_projects():
        """プロジェクト一覧を取得"""
        try:
            return await client.get_projects()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/api/projects/{project_code}/cases")
    async def get_test_cases(project_code: str):
        """テストケース一覧を取得"""
        try:
            return await client.get_test_cases(project_code)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/api/projects/{project_code}/cases")
    async def create_test_case(project_code: str, data: Dict[str, Any]):
        """テストケースを作成"""
        try:
            return await client.create_test_case(project_code, data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/api/projects/{project_code}/runs")
    async def get_test_runs(project_code: str):
        """テストラン一覧を取得"""
        try:
            return await client.get_test_runs(project_code)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/api/projects/{project_code}/runs")
    async def create_test_run(project_code: str, data: Dict[str, Any]):
        """テストランを作成"""
        try:
            return await client.create_test_run(project_code, data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return app 