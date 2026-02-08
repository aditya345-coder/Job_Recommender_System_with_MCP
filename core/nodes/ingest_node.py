import fitz
from typing import Dict, Any


def ingest_resume(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        uploaded_file = state.get("uploaded_file")
        if not uploaded_file:
            state["error"] = "No resume file provided"
            return state

        uploaded_file.seek(0)
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        state["resume_text"] = text
        state["error"] = None
    except Exception as e:
        state["error"] = f"Resume ingestion failed: {str(e)}"

    return state
