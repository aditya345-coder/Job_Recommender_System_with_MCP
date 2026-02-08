from typing import Dict, Any
import json
from ..llm import LLMService
from ..utils.skill_extractor import extract_skills_regex

llm = LLMService()

def extract_skills(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        resume_text = state.get("resume_text", "")

        try:
            # Try LLM Extraction first
            content = llm.get_completion(
                system_prompt="Extract all technical and soft skills from the resume. Return as a JSON object with a key 'skills' containing an array of strings.",
                user_prompt=resume_text,
                json_mode=True
            )
            skills_data = json.loads(content)
            state["skills"] = skills_data.get("skills", [])
            
        except Exception as llm_error:
            # Fallback to Regex Extraction
            print(f"LLM Skill Extraction failed ({llm_error}). Falling back to Keyword Matching...")
            skills = extract_skills_regex(resume_text)
            state["skills"] = skills
            if not skills:
                print("Warning: No skills found even with keyword matching.")

    except Exception as e:
        state["error"] = f"Skill extraction failed: {str(e)}"

    return state
