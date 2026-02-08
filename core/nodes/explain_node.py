from typing import Dict, Any
from ..llm import LLMService

llm = LLMService()

def explain_matches(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        matches = state.get("matches", [])

        explanations = []
        for match in matches:
            prompt = f"""
            Explain why this candidate is a good match for the job:
            
            Job Title: {match["title"]}
            Company: {match["company"]}
            Match Score: {match["match_score"]:.2%}
            Matched Skills: {", ".join(match["matched_skills"])}
            Missing Skills: {", ".join(match["missing_skills"])}
            
            Provide a concise, professional explanation.
            """

            explanation = llm.get_completion(
                system_prompt="You are a career advisor. Provide clear, professional explanations for job match recommendations.",
                user_prompt=prompt,
                json_mode=False
            )

            explanations.append(
                {
                    "job_title": match["title"],
                    "company": match["company"],
                    "explanation": explanation,
                }
            )

        state["explanations"] = explanations

    except Exception as e:
        state["error"] = f"Explanation generation failed: {str(e)}"

    return state
