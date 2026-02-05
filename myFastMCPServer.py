<<<<<<< HEAD
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b


if __name__ == "__main__":
=======
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
>>>>>>> e74f70099d643ad8290f59fa2c1e7ccd8ba9d65d
    mcp.run(transport="http", port=8000)