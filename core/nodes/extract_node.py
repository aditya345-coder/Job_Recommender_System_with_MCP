from typing import Dict, Any
import json
from ..llm import LLMService

llm = LLMService()

def extract_skills(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        resume_text = state.get("resume_text", "")

        content = llm.get_completion(
            system_prompt="Extract all technical and soft skills from the resume. Return as a JSON object with a key 'skills' containing an array of strings.",
            user_prompt=resume_text,
            json_mode=True
        )

        skills_data = json.loads(content)
        state["skills"] = skills_data.get("skills", [])

    except Exception as e:
        state["error"] = f"Skill extraction failed: {str(e)}"

    return state
