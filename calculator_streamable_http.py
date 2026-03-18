#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("calculator_streamable_http")

class AddInput(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")

@mcp.tool(
    name="add_numbers",
    annotations={
        "title": "Add Two Numbers",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def add_numbers(params: AddInput) -> str:
    """Add two numbers and return the result."""
    result = params.a + params.b
    return f"The sum of {params.a} and {params.b} is: {result}"

def main():
    mcp.run(transport="streamable_http", port=8001)

if __name__ == "__main__":
    main()
