from typing import List, Dict

SKILL_TO_ROLE_MAP = {
    "Python": ["Python Developer", "Data Scientist", "Backend Engineer"],
    "Java": ["Java Developer", "Backend Engineer"],
    "JavaScript": ["Frontend Developer", "Full Stack Developer", "Web Developer"],
    "React": ["Frontend Developer", "React Developer", "UI Engineer"],
    "Angular": ["Frontend Developer", "Angular Developer"],
    "Node.js": ["Backend Engineer", "Full Stack Developer"],
    "C++": ["C++ Developer", "Software Engineer", "Systems Programmer"],
    "SQL": ["Data Analyst", "Database Administrator", "Backend Engineer"],
    "Machine Learning": ["Machine Learning Engineer", "Data Scientist", "AI Engineer"],
    "TensorFlow": ["Machine Learning Engineer", "Data Scientist"],
    "AWS": ["Cloud Engineer", "DevOps Engineer", "Solutions Architect"],
    "Azure": ["Cloud Engineer", "DevOps Engineer"],
    # ... extensible
}

def infer_roles_dict(skills: List[str]) -> List[str]:
    """
    Infers job roles based on skills using a simple dictionary lookup.
    This is a fallback method when LLM inference fails.
    """
    inferred_roles = set()
    
    for skill in skills:
        roles = SKILL_TO_ROLE_MAP.get(skill)
        if roles:
            inferred_roles.update(roles)
            
    # Default if nothing found but we have generic skills like "Problem Solving"
    if not inferred_roles and skills:
        return ["Software Engineer"] # Safe default
        
    return list(inferred_roles)
