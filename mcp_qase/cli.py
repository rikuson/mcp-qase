import typer
from qaseio import Configuration

from .server import QaseMCPServer

app = typer.Typer()

@app.command()
def main(
    token: str = typer.Option(..., help="Qase API token", envvar="QASE_API_TOKEN"),
    host: str = typer.Option("https://api.qase.io/v1", help="Qase API host URL"),
    dev: bool = typer.Option(False, help="Run in development mode with MCP Inspector"),
):
    """Start the MCP server for Qase API"""
    # Configure Qase API client
    configuration = Configuration()
    configuration.host = host
    configuration.api_key["Token"] = token

    # Initialize server
    server = QaseMCPServer(token, configuration)
    
    try:
        if dev:
            from mcp.cli import run_dev
            run_dev(server.mcp)
        else:
            server.mcp.run()
    except KeyboardInterrupt:
        print("\nShutting down server...")

if __name__ == "__main__":
    app() 