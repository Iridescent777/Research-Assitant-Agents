#!/usr/bin/env python3
"""
Compile LaTeX via MCP server-shell using Agno MCPTools.
Usage:
  python mcp_compile.py --project_dir "D:\PJLAB\Agent\final_project\result\多智能体系统协作与协调_paper" --main_tex main.tex
  python mcp_compile.py --project_dir "D:\PJLAB\Agent\final_project\result\reinforcement_learning_paper" --main_tex main.tex

Requires:
  - agno (pip install agno)
  - npx available (Node.js) to launch @modelcontextprotocol/server-shell
"""

import argparse
import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools


async def run_mcp_compile(project_dir: str, main_tex: str) -> None:
    mcp_tools = MCPTools(command="npx -y @modelcontextprotocol/server-shell")
    await mcp_tools.connect()

    instructions = dedent(f"""
        You are a LaTeX build assistant. Use the shell MCP to:
        - cd "{project_dir}"
        - Run: pdflatex -interaction=nonstopmode {main_tex}
        - If .aux exists: bibtex {main_tex[:-4]}
        - Run: pdflatex -interaction=nonstopmode {main_tex}
        - Run: pdflatex -interaction=nonstopmode {main_tex}
        - Print a short summary with:
          * PDF size (if exists)
          * Last 40 lines of main.log (if exists)
        Notes:
        - For Chinese text ensure ctex is loaded; if packages are missing, MiKTeX should auto-install or preinstall via mpm.
    """)

    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[mcp_tools],
        instructions=instructions,
        show_tool_calls=True,
        markdown=True,
    )

    await agent.aprint_response("Compile the LaTeX project now.", stream=True)

    await mcp_tools.close()


def main() -> None:
    p = argparse.ArgumentParser(description="Compile LaTeX via MCP server-shell")
    p.add_argument("--project_dir", required=True, help="Absolute path to LaTeX project directory")
    p.add_argument("--main_tex", default="main.tex", help="Main .tex file name (default: main.tex)")
    args = p.parse_args()

    asyncio.run(run_mcp_compile(args.project_dir, args.main_tex))


if __name__ == "__main__":
    main()
