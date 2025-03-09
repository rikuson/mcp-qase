from typing import Any, Dict, List, Optional
from qaseio import ApiClient, Configuration
from qaseio.models import (
    TestCase,
    TestCaseCreate,
    Project,
    ProjectCreate,
    Defect,
    DefectCreate,
    Suite,
    SuiteCreate,
)

class QaseClient:
    def __init__(self, api_token: str, configuration: Configuration = None):
        if configuration is None:
            configuration = Configuration()
            configuration.api_key["Token"] = api_token
        self.client = ApiClient(configuration)

    def get_projects(self) -> List[Project]:
        """Get all projects"""
        response = self.client.call_api(
            "/project",
            "GET",
            response_type="List[Project]"
        )
        return response.data

    def create_project(self, data: ProjectCreate) -> Project:
        """Create a new project"""
        response = self.client.call_api(
            "/project",
            "POST",
            body=data.dict(),
            response_type="Project"
        )
        return response.data

    def get_test_cases(self, project_code: str) -> List[TestCase]:
        """Get all test cases for a project"""
        response = self.client.call_api(
            f"/case/{project_code}",
            "GET",
            response_type="List[TestCase]"
        )
        return response.data

    def create_test_case(self, project_code: str, data: TestCaseCreate) -> TestCase:
        """Create a new test case"""
        response = self.client.call_api(
            f"/case/{project_code}",
            "POST",
            body=data.dict(),
            response_type="TestCase"
        )
        return response.data

    def get_test_runs(self, project_code: str) -> List[Dict[str, Any]]:
        """Get all test runs for a project"""
        response = self.client.call_api(
            f"/run/{project_code}",
            "GET",
            response_type="List[Dict[str, Any]]"
        )
        return response.data

    def create_test_run(self, project_code: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new test run"""
        response = self.client.call_api(
            f"/run/{project_code}",
            "POST",
            body=data,
            response_type="Dict[str, Any]"
        )
        return response.data

    def get_defects(self, project_code: str) -> List[Defect]:
        """Get all defects for a project"""
        response = self.client.call_api(
            f"/defect/{project_code}",
            "GET",
            response_type="List[Defect]"
        )
        return response.data

    def create_defect(self, project_code: str, data: DefectCreate) -> Defect:
        """Create a new defect"""
        response = self.client.call_api(
            f"/defect/{project_code}",
            "POST",
            body=data.dict(),
            response_type="Defect"
        )
        return response.data

    def get_suites(self, project_code: str) -> List[Suite]:
        """Get all test suites for a project"""
        response = self.client.call_api(
            f"/suite/{project_code}",
            "GET",
            response_type="List[Suite]"
        )
        return response.data

    def create_suite(self, project_code: str, data: SuiteCreate) -> Suite:
        """Create a new test suite"""
        response = self.client.call_api(
            f"/suite/{project_code}",
            "POST",
            body=data.dict(),
            response_type="Suite"
        )
        return response.data 