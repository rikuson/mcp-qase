# MCP Qase API Server

MCP server implementation for Qase Test Management API.

## Installation

```bash
pip install mcp-qase
```

## Usage

```bash
uvx mcp-qase --url=<QASE_API_URL> --token=<QASE_API_TOKEN>
```

By default, the server starts at `http://127.0.0.1:8000`.

### Options

- `--url`: Qase API URL (required)
- `--token`: Qase API token (required)
- `--host`: Server host address (default: 127.0.0.1)
- `--port`: Server port number (default: 8000)

## API Endpoints

- `GET /api/projects`: Get list of projects
- `GET /api/projects/{project_code}/cases`: Get list of test cases
- `POST /api/projects/{project_code}/cases`: Create a new test case
- `GET /api/projects/{project_code}/runs`: Get list of test runs
- `POST /api/projects/{project_code}/runs`: Create a new test run

## Development

```bash
# Install dependencies
poetry install

# Start development server
poetry run mcp-qase --url=<QASE_API_URL> --token=<QASE_API_TOKEN>
```
