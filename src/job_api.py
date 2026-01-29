from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# fetch jobs from linkedin based on search query and location
def fetch_linkedin_jobs(serarch_query, location="India", rows=60):
    pass


# fetch jobs from naukri based on search query and location
def fetch_naukri_jobs(serarch_query, location="India", rows=60):
    pass