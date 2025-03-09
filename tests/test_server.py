import pytest
from unittest.mock import Mock, patch
from qaseio.models import Project, TestCase
from mcp_qase.server import QaseMCPServer

@pytest.fixture
def mock_client():
    with patch("mcp_qase.server.QaseClient") as mock:
        yield mock

@pytest.fixture
def server(mock_client):
    return QaseMCPServer("dummy-token")

@pytest.mark.asyncio
async def test_get_projects_resource(server):
    # Arrange
    mock_projects = [Project(id=1, title="Test Project", code="TEST")]
    server.client.get_projects.return_value = mock_projects

    # Act
    result = await server.mcp.get_resource("projects://")

    # Assert
    assert "Test Project" in result
    assert "TEST" in result

@pytest.mark.asyncio
async def test_get_test_cases_resource(server):
    # Arrange
    mock_cases = [TestCase(id=1, title="Test Case")]
    server.client.get_test_cases.return_value = mock_cases

    # Act
    result = await server.mcp.get_resource("projects://TEST/cases")

    # Assert
    assert "Test Case" in result

@pytest.mark.asyncio
async def test_create_project_tool(server):
    # Arrange
    mock_project = Project(id=1, title="New Project", code="NEW")
    server.client.create_project.return_value = mock_project

    # Act
    result = await server.mcp.invoke_tool("create_project", ["New Project", "NEW"])

    # Assert
    assert "New Project" in result
    assert "NEW" in result

@pytest.mark.asyncio
async def test_create_test_case_tool(server):
    # Arrange
    mock_case = TestCase(id=1, title="New Test Case")
    server.client.create_test_case.return_value = mock_case

    # Act
    result = await server.mcp.invoke_tool("create_test_case", ["TEST", "New Test Case"])

    # Assert
    assert "New Test Case" in result 