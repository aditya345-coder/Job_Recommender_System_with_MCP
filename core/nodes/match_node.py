from typing import Dict, Any

def match_jobs(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        skills = state.get("skills", [])
        jobs = state.get("jobs", [])

        matches = []
        for job in jobs:
            job_skills = job.get("required_skills", [])

            common_skills = set(skills) & set(job_skills)
            total_required = len(job_skills)
            match_score = (
                len(common_skills) / total_required if total_required > 0 else 0
            )

            match = {
                "job_id": job.get("id"),
                "title": job.get("title"),
                "company": job.get("company"),
                "location": job.get("location"),
                "match_score": match_score,
                "matched_skills": list(common_skills),
                "missing_skills": list(set(job_skills) - set(skills)),
            }
            matches.append(match)

        matches = sorted(matches, key=lambda x: x["match_score"], reverse=True)
        state["matches"] = matches[:10]

    except Exception as e:
        state["error"] = f"Job matching failed: {str(e)}"

    return state
