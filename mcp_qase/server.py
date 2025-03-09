from typing import List
from mcp.server.fastmcp import FastMCP
from qaseio import Configuration
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

from .client import QaseClient

class QaseMCPServer:
    def __init__(self, token: str, configuration: Configuration):
        self.client = QaseClient(token, configuration)
        self.mcp = FastMCP("Qase API")
        self._setup_resources()
        self._setup_tools()

    def _setup_resources(self):
        @self.mcp.resource("projects://")
        def get_projects():
            """Get all projects"""
            projects = self.client.get_projects()
            return [p.dict() for p in projects]

        @self.mcp.resource("projects://{project_code}/cases")
        def get_test_cases(project_code: str):
            """Get all test cases for a project"""
            cases = self.client.get_test_cases(project_code)
            return [c.dict() for c in cases]

        @self.mcp.resource("projects://{project_code}/runs")
        def get_test_runs(project_code: str):
            """Get all test runs for a project"""
            runs = self.client.get_test_runs(project_code)
            return runs

        @self.mcp.resource("projects://{project_code}/defects")
        def get_defects(project_code: str):
            """Get all defects for a project"""
            defects = self.client.get_defects(project_code)
            return [d.dict() for d in defects]

        @self.mcp.resource("projects://{project_code}/suites")
        def get_suites(project_code: str):
            """Get all test suites for a project"""
            suites = self.client.get_suites(project_code)
            return [s.dict() for s in suites]

    def _setup_tools(self):
        @self.mcp.tool("create_project")
        def create_project(title: str, code: str):
            """Create a new project"""
            data = ProjectCreate(title=title, code=code)
            project = self.client.create_project(data)
            return project.dict()

        @self.mcp.tool("create_test_case")
        def create_test_case(project_code: str, title: str):
            """Create a new test case"""
            data = TestCaseCreate(title=title)
            case = self.client.create_test_case(project_code, data)
            return case.dict()

        @self.mcp.tool("create_test_run")
        def create_test_run(project_code: str, title: str):
            """Create a new test run"""
            data = {"title": title}
            run = self.client.create_test_run(project_code, data)
            return run

        @self.mcp.tool("create_defect")
        def create_defect(project_code: str, title: str):
            """Create a new defect"""
            data = DefectCreate(title=title)
            defect = self.client.create_defect(project_code, data)
            return defect.dict()

        @self.mcp.tool("create_suite")
        def create_suite(project_code: str, title: str):
            """Create a new test suite"""
            data = SuiteCreate(title=title)
            suite = self.client.create_suite(project_code, data)
            return suite.dict()
