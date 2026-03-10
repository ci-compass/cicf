#!/usr/bin/env python3

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

def get_s3_client():
    session = boto3.session.Session()
    return session.client('s3',
                         region_name=REGION,
                         endpoint_url=ENDPOINT_URL,
                         aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)

def main():
    if not ACCESS_KEY or not SECRET_KEY:
        print("Error: DO_SPACES_KEY and DO_SPACES_SECRET must be set in data/.env")
        return

    # Check for prefix argument
    prefix = sys.argv[1] if len(sys.argv) > 1 else ''

    s3 = get_s3_client()
    
    print(f"Listing contents of bucket: '{BUCKET_NAME}'" + (f" (prefix: '{prefix}')" if prefix else ""))
    print("-" * 60)
    print(f"{'Key':<40} | {'Size (KB)':>10} | {'Last Modified'}")
    print("-" * 60)

    try:
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=BUCKET_NAME, Prefix=prefix)

        count = 0
        total_size = 0
        
        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    size_kb = obj['Size'] / 1024
                    last_modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M')
                    
                    print(f"{key:<40} | {size_kb:>10.2f} | {last_modified}")
                    
                    count += 1
                    total_size += obj['Size']
            else:
                print("No objects found.")
                return

        print("-" * 60)
        print(f"Total Objects: {count}")
        print(f"Total Size:    {total_size / (1024*1024):.2f} MB")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
