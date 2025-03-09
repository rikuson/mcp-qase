import typer
import uvicorn
from typing import Optional

app = typer.Typer()

@app.command()
def main(
    url: str = typer.Option(..., help="Qase API URL"),
    token: str = typer.Option(..., help="Qase API token"),
    host: str = typer.Option("127.0.0.1", help="Host to bind the server to"),
    port: int = typer.Option(8000, help="Port to bind the server to"),
):
    """Start the MCP server for Qase API"""
    from .server import create_app
    api_app = create_app(url, token)
    uvicorn.run(api_app, host=host, port=port)

if __name__ == "__main__":
    app() 