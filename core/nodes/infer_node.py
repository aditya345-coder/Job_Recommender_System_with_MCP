from typing import Dict, Any
import json
from ..llm import LLMService
from ..utils.role_mapper import infer_roles_dict

llm = LLMService()

def infer_roles(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        skills = state.get("skills", [])

        try:
            # Try LLM Inference first
            content = llm.get_completion(
                system_prompt="Based on the extracted skills, infer the most suitable job roles. Return as a JSON object with a key 'roles' containing an array of role titles.",
                user_prompt=f"Skills: {', '.join(skills)}",
                json_mode=True
            )
            roles_data = json.loads(content)
            state["roles"] = roles_data.get("roles", [])
            
        except Exception as llm_error:
            # Fallback to Dictionary Mapping
            print(f"LLM Role Inference failed ({llm_error}). Falling back to Dictionary Mapping...")
            roles = infer_roles_dict(skills)
            state["roles"] = roles

    except Exception as e:
        state["error"] = f"Role inference failed: {str(e)}"

    return state
