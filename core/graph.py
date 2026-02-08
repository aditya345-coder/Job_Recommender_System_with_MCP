from typing import TypedDict, List, Optional, Annotated, Any
from langgraph.graph import StateGraph, END


class ResumeState(TypedDict):
    uploaded_file: Optional[Any]
    resume_text: str
    skills: List[str]
    roles: List[str]
    jobs: List[dict]
    matches: List[dict]
    explanations: List[dict]
    error: Optional[str]


class ResumeGraph:
    def __init__(self):
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        workflow = StateGraph(ResumeState)

        from .nodes.ingest_node import ingest_resume
        from .nodes.extract_node import extract_skills
        from .nodes.infer_node import infer_roles
        from .nodes.provider_node import fetch_jobs
        from .nodes.match_node import match_jobs
        from .nodes.explain_node import explain_matches

        workflow.add_node("ingest", ingest_resume)
        workflow.add_node("extract", extract_skills)
        workflow.add_node("infer", infer_roles)
        workflow.add_node("provider", fetch_jobs)
        workflow.add_node("match", match_jobs)
        workflow.add_node("explain", explain_matches)

        workflow.set_entry_point("ingest")
        workflow.add_edge("ingest", "extract")
        workflow.add_edge("extract", "infer")
        workflow.add_edge("infer", "provider")
        workflow.add_edge("provider", "match")
        workflow.add_edge("match", "explain")
        workflow.add_edge("explain", END)

        return workflow.compile()

    def invoke(self, initial_state: ResumeState) -> ResumeState:
        return self.graph.invoke(initial_state)
