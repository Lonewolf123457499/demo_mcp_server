import os
import subprocess
from fastmcp import FastMCP

# -------------------------------------------------------------------
# MCP Initialization
# -------------------------------------------------------------------

mcp = FastMCP("terminal")

DEFAULT_WORKSPACE = "/Users/vedantsingh/Desktop/mcp/mcp_sse/workspace"

# -------------------------------------------------------------------
# TOOL 1: run_command
# -------------------------------------------------------------------

@mcp.tool()
async def run_command(command: str, cwd: str = DEFAULT_WORKSPACE) -> str:
    """
    Execute a shell command and return its output.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30
        )
        return f"Exit code: {result.returncode}\nOutput: {result.stdout}\nError: {result.stderr}"
    except subprocess.TimeoutExpired:
        return "Command timed out"
    except Exception as e:
        return f"Error executing command: {str(e)}"

# -------------------------------------------------------------------
# TOOL 2: add_numbers
# -------------------------------------------------------------------

@mcp.tool()
async def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers.
    """
    return a + b

# -------------------------------------------------------------------
# Run MCP Server (Modern HTTP Transport)
# -------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(
        transport="http",   # 🔥 NEW (replaces SSE)
        host="0.0.0.0",
        port=8001
    )