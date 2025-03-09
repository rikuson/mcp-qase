import pytest
from unittest.mock import Mock, patch
from qaseio.models import Project, TestCase, TestRun
from mcp_qase.client import QaseClient

@pytest.fixture
def mock_qase_api():
    with patch("mcp_qase.client.QaseApi") as mock:
        yield mock

@pytest.fixture
def client(mock_qase_api):
    return QaseClient("dummy-token")

@pytest.mark.asyncio
async def test_get_projects(client, mock_qase_api):
    # Arrange
    mock_response = Mock()
    mock_response.data = [Project(id=1, title="Test Project", code="TEST")]
    mock_qase_api.return_value.projects.get_all.return_value = mock_response

    # Act
    result = await client.get_projects()

    # Assert
    assert len(result) == 1
    assert result[0].title == "Test Project"
    assert result[0].code == "TEST"

@pytest.mark.asyncio
async def test_get_test_cases(client, mock_qase_api):
    # Arrange
    mock_response = Mock()
    mock_response.data = [TestCase(id=1, title="Test Case")]
    mock_qase_api.return_value.cases.get_all.return_value = mock_response

    # Act
    result = await client.get_test_cases("TEST")

    # Assert
    assert len(result) == 1
    assert result[0].title == "Test Case"

@pytest.mark.asyncio
async def test_get_test_runs(client, mock_qase_api):
    # Arrange
    mock_response = Mock()
    mock_response.data = [TestRun(id=1, title="Test Run")]
    mock_qase_api.return_value.runs.get_all.return_value = mock_response

    # Act
    result = await client.get_test_runs("TEST")

    # Assert
    assert len(result) == 1
    assert result[0].title == "Test Run" 