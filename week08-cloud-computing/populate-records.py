#!/usr/bin/env python3

import requests
import json
import os
import sys

# Configuration
# OpenAlex API recommends adding an email for the "polite pool"
EMAIL = "" # Replace with your email address
BASE_URL = "https://api.openalex.org/works"
DEFAULT_QUERY = "gravational waves"
PER_PAGE = 25  # Number of works per API call
TOTAL_PAGES = 4
TOTAL_RECORDS = PER_PAGE * TOTAL_PAGES  # Total 100 works for this exercise
TARGET_DIRECTORY = os.path.join(os.getcwd(), "openalex-records")

def fetch_page(page, query):
    """Fetch a single page of results from OpenAlex."""
    params = {
        'search': query,
        'per_page': PER_PAGE,
        'page': page,
        'mailto': EMAIL
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error fetching page {page}: {response.status_code}")
        return []

def main():
    # Use command line argument if provided, otherwise use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = DEFAULT_QUERY

    print(f"Pulling records from OpenAlex for query: '{query}'")

    if EMAIL == "":
        print("Set the EMAIL variable in the script and run again.")
        sys.exit(1)
    
    # make sure the target directory exists
    os.makedirs(TARGET_DIRECTORY, exist_ok=True)
    
    for page in range(1, TOTAL_PAGES + 1):
        print(f"Fetching page {page}...")
        works = fetch_page(page, query)

        for w in works:
            work_id = w["id"].split("/")[-1]  # the W identifier is last in the URL
            target_filename = os.path.join(TARGET_DIRECTORY, work_id + ".json")
            with open(target_filename, "w") as f:
                json.dump(w, f, indent=4)
        
if __name__ == "__main__":
    main()
