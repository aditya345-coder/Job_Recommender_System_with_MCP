import re
from typing import List

# A basic list of common technical and soft skills to check for
COMMON_SKILLS_DB = {
    # Languages
    "Python", "Java", "C++", "JavaScript", "TypeScript", "HTML", "CSS", "SQL", "Go", "Rust", "Swift", "Kotlin", "PHP", "Ruby",
    # Frameworks/Libs
    "React", "Angular", "Vue", "Node.js", "Django", "Flask", "FastAPI", "Spring Boot", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn",
    # Cloud/DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform", "Jenkins", "CI/CD", "Git", "GitHub", "Linux",
    # Databases
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "Oracle", "DynamoDB",
    # Soft Skills
    "Communication", "Leadership", "Teamwork", "Problem Solving", "Critical Thinking", "Agile", "Scrum", "Project Management"
}

def extract_skills_regex(text: str) -> List[str]:
    """
    Extracts skills from text using simple keyword matching against a predefined list.
    This is a fallback method when LLM extraction fails.
    """
    found_skills = set()
    text_lower = text.lower()
    
    for skill in COMMON_SKILLS_DB:
        # Simple word boundary check to avoid partial matches (e.g., 'Go' in 'Google')
        # Escaping skill for regex safety
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)
            
    return list(found_skills)
