#!/usr/bin/env python 

import os
import boto3
import json
from dotenv import load_dotenv

# Load environment variables for credentials
load_dotenv('.env')

# Configuration
REGION = 'nyc3'
ENDPOINT_URL = f'https://{REGION}.digitaloceanspaces.com'
BUCKET_NAME = os.getenv('DO_SPACES_BUCKET', 'cicf')
ACCESS_KEY = os.getenv('DO_SPACES_KEY')
SECRET_KEY = os.getenv('DO_SPACES_SECRET')
SOURCE_DIR = 'openalex-records'

def get_s3_client():
    session = boto3.session.Session()
    return session.client('s3',
                         region_name=REGION,
                         endpoint_url=ENDPOINT_URL,
                         aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)

def main():
    if not ACCESS_KEY or not SECRET_KEY:
        print("Error: DO_SPACES_KEY and DO_SPACES_SECRET must be set in .env")
        return

    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Directory '{SOURCE_DIR}' not found. Run populate-records.py first.")
        return

    # Get list of JSON files
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.json')]
    if not files:
        print(f"No JSON files found in {SOURCE_DIR}")
        return

    # Split files into 4 groups
    num_groups = 4
    # Calculate group size (ceiling division)
    group_size = len(files) // num_groups
    
    s3 = get_s3_client()
    print(f"Uploading {len(files)} files to bucket '{BUCKET_NAME}' in {num_groups} groups...")

    start_index = 0
    for i in range(num_groups):
        end = start_index + group_size
        group_files = files[start_index:end]
        start_index += group_size

        prefix = f"group{i+1}/"
        
        print(f"Processing {prefix} ({len(group_files)} files)...")
        
        for filename in group_files:
            local_path = os.path.join(SOURCE_DIR, filename)
            s3_path = prefix + filename
            
            try:
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
            except Exception as e:
                print(f"  Failed to upload {filename}: {e}")

    print("\nUpload complete.")

if __name__ == "__main__":
    main()
