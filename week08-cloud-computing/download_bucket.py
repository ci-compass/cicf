#!/usr/bin/env python3

import json
import os
import boto3
import sys
from dotenv import load_dotenv

# Load environment variables for credentials
load_dotenv('.env')

# Configuration
REGION = 'nyc3'
ENDPOINT_URL = f'https://{REGION}.digitaloceanspaces.com'
BUCKET_NAME = os.getenv('DO_SPACES_BUCKET', 'cicf-object-store')
ACCESS_KEY = os.getenv('DO_SPACES_KEY')
SECRET_KEY = os.getenv('DO_SPACES_SECRET')

TARGET_DIRECTORY = os.path.join(os.getcwd(), "openalex-records")

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

    # Take prefix as argument (e.g., group1/)
    prefix = sys.argv[1] if len(sys.argv) > 1 else ''
    if prefix != '' and not prefix.endswith('/'):
        prefix += '/'

    # make sure the target directory exists
    os.makedirs(TARGET_DIRECTORY, exist_ok=True)
    
    s3 = get_s3_client()

    print(f"Downloading from bucket '{BUCKET_NAME}' with prefix '{prefix}'...")

    try:
        # List objects in the prefix
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=BUCKET_NAME, Prefix=prefix)
        
        for page in pages:
            if not 'Contents' in page:
                print("No objects found to download.")
                break
            for obj in page['Contents']:
                key = obj['Key']
                # 1. Determine local path
                local_path = os.path.join(TARGET_DIRECTORY, key)
                
                # 2. CREATE DIRECTORIES if they don't exist
                local_dir = os.path.dirname(local_path)
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir, exist_ok=True)
                
                # 3. Download the file
                print(f"  Downloading {key} -> {local_path}")
                s3.download_file(BUCKET_NAME, key, local_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

