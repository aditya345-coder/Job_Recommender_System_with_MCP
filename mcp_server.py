from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP
from core.graph import ResumeGraph, ResumeState

mcp = FastMCP("Job Recommender")


@mcp.tool()
async def analyze_resume(resume_content: str) -> dict:
    graph = ResumeGraph()
    initial_state = ResumeState(
        uploaded_file=None,
        resume_text=resume_content,
        skills=[],
        roles=[],
        jobs=[],
        matches=[],
        explanations=[],
        error=None,
    )
    result = graph.invoke(initial_state)
    return {
        "skills": result.get("skills", []),
        "roles": result.get("roles", []),
        "matches": result.get("matches", []),
        "explanations": result.get("explanations", []),
        "error": result.get("error"),
    }


@mcp.tool()
async def infer_roles(skills: list) -> dict:
    from core.nodes.infer_node import infer_roles

    state = {"skills": skills, "roles": [], "error": None}
    result = infer_roles(state)
    return {"roles": result.get("roles", []), "error": result.get("error")}


@mcp.tool()
async def match_jobs(skills: list, job_descriptions: list) -> dict:
    from core.nodes.match_node import match_jobs

    state = {"skills": skills, "jobs": job_descriptions, "matches": [], "error": None}
    result = match_jobs(state)
    return {"matches": result.get("matches", []), "error": result.get("error")}


@mcp.tool()
async def explain_match(match_data: dict) -> dict:
    from core.nodes.explain_node import explain_matches

    state = {"matches": [match_data], "explanations": [], "error": None}
    result = explain_matches(state)
    return {
        "explanation": result.get("explanations", [{}])[0],
        "error": result.get("error"),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
