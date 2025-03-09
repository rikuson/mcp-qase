from typing import Any, Dict, List, Optional
from qaseio.client import QaseApi
from qaseio.models import (
    TestCase,
    TestCaseCreate,
    TestRun,
    TestRunCreate,
    Project,
    ProjectCreate,
    Defect,
    DefectCreate,
    Suite,
    SuiteCreate,
)

class QaseClient:
    def __init__(self, api_token: str):
        self.client = QaseApi(api_token)

    async def get_projects(self) -> List[Project]:
        """Get all projects"""
        response = self.client.projects.get_all()
        return response.data

    async def create_project(self, data: ProjectCreate) -> Project:
        """Create a new project"""
        response = self.client.projects.create(data)
        return response.data

    async def get_test_cases(self, project_code: str) -> List[TestCase]:
        """Get all test cases for a project"""
        response = self.client.cases.get_all(project_code)
        return response.data

    async def create_test_case(self, project_code: str, data: TestCaseCreate) -> TestCase:
        """Create a new test case"""
        response = self.client.cases.create(project_code, data)
        return response.data

    async def get_test_runs(self, project_code: str) -> List[TestRun]:
        """Get all test runs for a project"""
        response = self.client.runs.get_all(project_code)
        return response.data

    async def create_test_run(self, project_code: str, data: TestRunCreate) -> TestRun:
        """Create a new test run"""
        response = self.client.runs.create(project_code, data)
        return response.data

    async def get_defects(self, project_code: str) -> List[Defect]:
        """Get all defects for a project"""
        response = self.client.defects.get_all(project_code)
        return response.data

    async def create_defect(self, project_code: str, data: DefectCreate) -> Defect:
        """Create a new defect"""
        response = self.client.defects.create(project_code, data)
        return response.data

    async def get_suites(self, project_code: str) -> List[Suite]:
        """Get all test suites for a project"""
        response = self.client.suites.get_all(project_code)
        return response.data

    async def create_suite(self, project_code: str, data: SuiteCreate) -> Suite:
        """Create a new test suite"""
        response = self.client.suites.create(project_code, data)
        return response.data 