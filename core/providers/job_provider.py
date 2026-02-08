from typing import List, Dict, Any
import os
from .apify_provider import ApifyJobProvider


class JobProvider:
    def __init__(self):
        self.apify_provider = ApifyJobProvider()
        self.use_apify = os.getenv("APIFY_API_TOKEN") is not None and os.getenv("APIFY_API_TOKEN") != ""
        
        self.mock_jobs = {
            "Software Engineer": [
                {
                    "id": 1,
                    "title": "Senior Software Engineer",
                    "company": "TechCorp",
                    "location": "Remote",
                    "required_skills": [
                        "Python",
                        "JavaScript",
                        "React",
                        "SQL",
                        "Git",
                        "AWS",
                    ],
                },
                {
                    "id": 2,
                    "title": "Full Stack Developer",
                    "company": "InnovateHub",
                    "location": "New York",
                    "required_skills": [
                        "Python",
                        "Django",
                        "React",
                        "PostgreSQL",
                        "Docker",
                        "REST APIs",
                    ],
                },
            ],
            "Data Scientist": [
                {
                    "id": 3,
                    "title": "Senior Data Scientist",
                    "company": "DataDrive",
                    "location": "San Francisco",
                    "required_skills": [
                        "Python",
                        "Machine Learning",
                        "TensorFlow",
                        "SQL",
                        "Statistics",
                        "Pandas",
                    ],
                },
                {
                    "id": 4,
                    "title": "ML Engineer",
                    "company": "AI Solutions",
                    "location": "Remote",
                    "required_skills": [
                        "Python",
                        "PyTorch",
                        "Deep Learning",
                        "MLOps",
                        "Docker",
                        "Kubernetes",
                    ],
                },
            ],
            "Product Manager": [
                {
                    "id": 5,
                    "title": "Senior Product Manager",
                    "company": "ProductLabs",
                    "location": "Boston",
                    "required_skills": [
                        "Agile",
                        "Scrum",
                        "User Research",
                        "Roadmap Planning",
                        "Analytics",
                        "Stakeholder Management",
                    ],
                }
            ],
            "DevOps Engineer": [
                {
                    "id": 6,
                    "title": "Senior DevOps Engineer",
                    "company": "CloudOps",
                    "location": "Seattle",
                    "required_skills": [
                        "AWS",
                        "Kubernetes",
                        "Docker",
                        "Terraform",
                        "CI/CD",
                        "Linux",
                    ],
                }
            ],
            "Machine Learning Engineer": [
                {
                    "id": 7,
                    "title": "ML Platform Engineer",
                    "company": "MLScale",
                    "location": "Austin",
                    "required_skills": [
                        "Python",
                        "MLOps",
                        "Kubernetes",
                        "TensorFlow",
                        "Docker",
                        "Airflow",
                    ],
                }
            ],
        }

    def get_jobs_for_role(self, role: str) -> List[Dict]:
        if self.use_apify:
            print(f"Fetching real jobs for role: {role} using Apify...")
            try:
                jobs = self.apify_provider.get_jobs(role)
                if jobs:
                    return jobs
                print(f"Apify returned no jobs for {role}, falling back to mock data...")
            except Exception as e:
                print(f"Apify fetch failed for {role}: {e}. Falling back to mock data...")
        
        print(f"Using mock jobs for role: {role}...")
        jobs = self.mock_jobs.get(role, [])

        if not jobs:
            fallback_jobs = [
                {
                    "id": 99,
                    "title": role,
                    "company": "TechCompany",
                    "location": "Remote",
                    "required_skills": ["Python", "Problem Solving", "Communication"],
                }
            ]
            return fallback_jobs

        return jobs
