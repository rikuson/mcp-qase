import pytest
import asyncio
from unittest.mock import Mock, patch
from qaseio.models import Project, TestCase
from mcp_qase.server import QaseMCPServer

@pytest.fixture
def mock_client():
    with patch("mcp_qase.server.QaseClient") as mock:
        yield mock

@pytest.fixture
async def server(mock_client):
    server = QaseMCPServer("dummy-token")
    yield server

@pytest.mark.asyncio
async def test_process_get_projects(server):
    # Arrange
    mock_projects = [Project(id=1, title="Test Project", code="TEST")]
    server.client.get_projects.return_value = mock_projects

    # Act
    result = await server._process_message("GET_PROJECTS")

    # Assert
    assert "OK" in result
    assert "Test Project" in result
    assert "TEST" in result

@pytest.mark.asyncio
async def test_process_get_cases(server):
    # Arrange
    mock_cases = [TestCase(id=1, title="Test Case")]
    server.client.get_test_cases.return_value = mock_cases

    # Act
    result = await server._process_message("GET_CASES TEST")

    # Assert
    assert "OK" in result
    assert "Test Case" in result

@pytest.mark.asyncio
async def test_process_invalid_command(server):
    # Act
    result = await server._process_message("INVALID_COMMAND")

    # Assert
    assert "ERROR" in result
    assert "Unknown command" in result

@pytest.mark.asyncio
async def test_process_empty_message(server):
    # Act
    result = await server._process_message("")

    # Assert
    assert "ERROR" in result
    assert "Empty message" in result 