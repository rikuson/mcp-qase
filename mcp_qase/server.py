import asyncio
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP, Context
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

from .client import QaseClient

class QaseMCPServer:
    def __init__(self, token: str):
        self.client = QaseClient(token)
        self.mcp = FastMCP("Qase API")
        self._setup_resources()
        self._setup_tools()

    def _setup_resources(self):
        @self.mcp.resource("projects://")
        async def get_projects() -> str:
            """Get all projects"""
            projects = await self.client.get_projects()
            return str([p.dict() for p in projects])

        @self.mcp.resource("projects://{project_code}/cases")
        async def get_test_cases(project_code: str) -> str:
            """Get all test cases for a project"""
            cases = await self.client.get_test_cases(project_code)
            return str([c.dict() for c in cases])

        @self.mcp.resource("projects://{project_code}/runs")
        async def get_test_runs(project_code: str) -> str:
            """Get all test runs for a project"""
            runs = await self.client.get_test_runs(project_code)
            return str([r.dict() for r in runs])

        @self.mcp.resource("projects://{project_code}/defects")
        async def get_defects(project_code: str) -> str:
            """Get all defects for a project"""
            defects = await self.client.get_defects(project_code)
            return str([d.dict() for d in defects])

        @self.mcp.resource("projects://{project_code}/suites")
        async def get_suites(project_code: str) -> str:
            """Get all test suites for a project"""
            suites = await self.client.get_suites(project_code)
            return str([s.dict() for s in suites])

    def _setup_tools(self):
        @self.mcp.tool()
        async def create_project(title: str, code: str) -> str:
            """Create a new project"""
            data = ProjectCreate(title=title, code=code)
            project = await self.client.create_project(data)
            return str(project.dict())

        @self.mcp.tool()
        async def create_test_case(project_code: str, title: str) -> str:
            """Create a new test case"""
            data = TestCaseCreate(title=title)
            case = await self.client.create_test_case(project_code, data)
            return str(case.dict())

        @self.mcp.tool()
        async def create_test_run(project_code: str, title: str) -> str:
            """Create a new test run"""
            data = TestRunCreate(title=title)
            run = await self.client.create_test_run(project_code, data)
            return str(run.dict())

        @self.mcp.tool()
        async def create_defect(project_code: str, title: str) -> str:
            """Create a new defect"""
            data = DefectCreate(title=title)
            defect = await self.client.create_defect(project_code, data)
            return str(defect.dict())

        @self.mcp.tool()
        async def create_suite(project_code: str, title: str) -> str:
            """Create a new test suite"""
            data = SuiteCreate(title=title)
            suite = await self.client.create_suite(project_code, data)
            return str(suite.dict())

    async def start(self, host: str = "127.0.0.1", port: int = 8000):
        """Start the MCP server"""
        await self.mcp.serve(host=host, port=port)

    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """Handle client connection"""
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break

                message = data.decode()
                response = await self._process_message(message)
                writer.write(response.encode())
                await writer.drain()
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            writer.close()
            await writer.wait_closed()

    async def _process_message(self, message: str) -> str:
        """Process incoming MCP message"""
        try:
            # Parse message and route to appropriate handler
            # This is a simplified example - you would need to implement proper MCP protocol parsing
            parts = message.split()
            if not parts:
                return "ERROR: Empty message"

            command = parts[0]
            args = parts[1:]

            handlers = {
                "GET_PROJECTS": self._handle_get_projects,
                "CREATE_PROJECT": self._handle_create_project,
                "GET_CASES": self._handle_get_cases,
                "CREATE_CASE": self._handle_create_case,
                "GET_RUNS": self._handle_get_runs,
                "CREATE_RUN": self._handle_create_run,
                "GET_DEFECTS": self._handle_get_defects,
                "CREATE_DEFECT": self._handle_create_defect,
                "GET_SUITES": self._handle_get_suites,
                "CREATE_SUITE": self._handle_create_suite,
            }

            handler = handlers.get(command)
            if not handler:
                return f"ERROR: Unknown command {command}"

            result = await handler(*args)
            return f"OK {result}"

        except Exception as e:
            return f"ERROR: {str(e)}"

    async def _handle_get_projects(self) -> str:
        """Handle GET_PROJECTS command"""
        projects = await self.client.get_projects()
        return str([p.dict() for p in projects])

    async def _handle_create_project(self, *args) -> str:
        """Handle CREATE_PROJECT command"""
        if len(args) < 2:
            return "ERROR: Missing project data"
        data = ProjectCreate(title=args[0], code=args[1])
        project = await self.client.create_project(data)
        return str(project.dict())

    async def _handle_get_cases(self, project_code: str) -> str:
        """Handle GET_CASES command"""
        cases = await self.client.get_test_cases(project_code)
        return str([c.dict() for c in cases])

    async def _handle_create_case(self, project_code: str, title: str, *args) -> str:
        """Handle CREATE_CASE command"""
        data = TestCaseCreate(title=title)
        case = await self.client.create_test_case(project_code, data)
        return str(case.dict())

    # Similar handlers for other commands... 