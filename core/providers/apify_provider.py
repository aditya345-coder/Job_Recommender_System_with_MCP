import os
import logging
from typing import List, Dict, Any
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class ApifyJobProvider:
    def __init__(self):
        self.api_token = os.getenv("APIFY_API_TOKEN")
        if self.api_token:
            self.client = ApifyClient(self.api_token)
        else:
            self.client = None
            logger.warning("APIFY_API_TOKEN not found in environment variables.")

        # Default Actor IDs - can be overridden by environment variables
        self.actors = {
            "linkedin": os.getenv("APIFY_LINKEDIN_ACTOR", "apify/linkedin-jobs-scraper"),
            "glassdoor": os.getenv("APIFY_GLASSDOOR_ACTOR", "apify/glassdoor-scraper"),
            "naukri": os.getenv("APIFY_NAUKRI_ACTOR", "muhammetakkurtt/naukri-job-scraper"),
            "freelancer": os.getenv("APIFY_FREELANCER_ACTOR", "jupri/freelancer-scraper"),
        }

    def fetch_linkedin_jobs(self, role: str, limit: int = 5) -> List[Dict]:
        if not self.client: return []
        try:
            run_input = {
                "queries": [role],
                "limitPerQuery": limit,
            }
            run = self.client.actor(self.actors["linkedin"]).call(run_input=run_input)
            jobs = []
            for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
                jobs.append({
                    "id": item.get("id", item.get("url")),
                    "title": item.get("title") or item.get("jobTitle"),
                    "company": item.get("companyName") or item.get("company"),
                    "location": item.get("location"),
                    "required_skills": item.get("skills", []),
                    "url": item.get("url"),
                    "source": "LinkedIn"
                })
            return jobs
        except Exception as e:
            logger.error(f"Error fetching LinkedIn jobs: {e}")
            return []

    def fetch_glassdoor_jobs(self, role: str, limit: int = 5) -> List[Dict]:
        if not self.client: return []
        try:
            run_input = {
                "queries": [role],
                "limitPerQuery": limit,
            }
            run = self.client.actor(self.actors["glassdoor"]).call(run_input=run_input)
            jobs = []
            for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
                jobs.append({
                    "id": item.get("id", item.get("url")),
                    "title": item.get("jobTitle") or item.get("title"),
                    "company": item.get("companyName") or item.get("company"),
                    "location": item.get("location"),
                    "required_skills": item.get("skills", []),
                    "url": item.get("url"),
                    "source": "Glassdoor"
                })
            return jobs
        except Exception as e:
            logger.error(f"Error fetching Glassdoor jobs: {e}")
            return []

    def fetch_naukri_jobs(self, role: str, limit: int = 5) -> List[Dict]:
        if not self.client: return []
        try:
            run_input = {
                "searchQuery": role,
                "maxItems": limit,
            }
            run = self.client.actor(self.actors["naukri"]).call(run_input=run_input)
            jobs = []
            for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
                jobs.append({
                    "id": item.get("id", item.get("jobId")),
                    "title": item.get("title") or item.get("jobTitle"),
                    "company": item.get("companyName") or item.get("company"),
                    "location": item.get("location"),
                    "required_skills": item.get("skills", []),
                    "url": item.get("url") or item.get("jdUrl"),
                    "source": "Naukri"
                })
            return jobs
        except Exception as e:
            logger.error(f"Error fetching Naukri jobs: {e}")
            return []

    def fetch_freelancer_jobs(self, role: str, limit: int = 5) -> List[Dict]:
        if not self.client: return []
        try:
            run_input = {
                "query": role,
                "maxItems": limit,
            }
            run = self.client.actor(self.actors["freelancer"]).call(run_input=run_input)
            jobs = []
            for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
                jobs.append({
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "company": item.get("employer", {}).get("username", "N/A"),
                    "location": "Remote",
                    "required_skills": [s.get("name") for s in item.get("jobs", []) if s.get("name")],
                    "url": f"https://www.freelancer.com/projects/{item.get('seo_url')}",
                    "source": "Freelancer"
                })
            return jobs
        except Exception as e:
            logger.error(f"Error fetching Freelancer jobs: {e}")
            return []

    def get_jobs(self, role: str, limit_per_provider: int = 3) -> List[Dict]:
        from concurrent.futures import ThreadPoolExecutor
        all_jobs = []
        
        fetchers = [
            (self.fetch_linkedin_jobs, (role, limit_per_provider)),
            (self.fetch_glassdoor_jobs, (role, limit_per_provider)),
            (self.fetch_naukri_jobs, (role, limit_per_provider)),
            (self.fetch_freelancer_jobs, (role, limit_per_provider)),
        ]
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(func, *args) for func, args in fetchers]
            for future in futures:
                try:
                    jobs = future.result()
                    all_jobs.extend(jobs)
                except Exception as e:
                    logger.error(f"Fetcher thread failed: {e}")
        
        return all_jobs
