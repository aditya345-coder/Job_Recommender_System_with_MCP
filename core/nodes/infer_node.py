from typing import Dict, Any
import json
from ..llm import LLMService

llm = LLMService()

def infer_roles(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        skills = state.get("skills", [])

        content = llm.get_completion(
            system_prompt="Based on the extracted skills, infer the most suitable job roles. Return as a JSON object with a key 'roles' containing an array of role titles.",
            user_prompt=f"Skills: {', '.join(skills)}",
            json_mode=True
        )

        roles_data = json.loads(content)
        state["roles"] = roles_data.get("roles", [])

    except Exception as e:
        state["error"] = f"Role inference failed: {str(e)}"

    return state
