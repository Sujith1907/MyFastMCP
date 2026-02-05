from fastmcp import FastMCP

mcp = FastMCP(name="My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)