from typing import Dict, Any
from core.providers.job_provider import JobProvider


def fetch_jobs(state: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if state.get("error"):
            return state

        roles = state.get("roles", [])
        provider = JobProvider()

        all_jobs = []
        for role in roles:
            jobs = provider.get_jobs_for_role(role)
            all_jobs.extend(jobs)

        state["jobs"] = all_jobs

    except Exception as e:
        state["error"] = f"Job fetching failed: {str(e)}"

    return state
