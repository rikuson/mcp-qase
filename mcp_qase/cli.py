import asyncio
import typer
from typing import Optional
from mcp.server.fastmcp import FastMCP

from .server import QaseMCPServer

app = typer.Typer()

@app.command()
def main(
    token: str = typer.Option(..., help="Qase API token", envvar="QASE_API_TOKEN"),
    host: str = typer.Option("127.0.0.1", help="Host to bind the server to"),
    port: int = typer.Option(8000, help="Port to bind the server to"),
    dev: bool = typer.Option(False, help="Run in development mode with MCP Inspector"),
):
    """Start the MCP server for Qase API"""
    server = QaseMCPServer(token)
    try:
        if dev:
            from mcp.cli import run_dev
            run_dev(server.mcp)
        else:
            asyncio.run(server.start(host, port))
    except KeyboardInterrupt:
        print("\nShutting down server...")

if __name__ == "__main__":
    app() 