#!/usr/bin/env python3

import os
import boto3
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

ACCESS_KEY = os.getenv('DO_SPACES_KEY')
SECRET_KEY = os.getenv('DO_SPACES_SECRET')
ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com' # Or your region
BUCKET_NAME = os.getenv('DO_SPACES_BUCKET')
FILE_NAME = 'NEON_count-mosquitoes.tar.gz'

session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url=ENDPOINT_URL,
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

try:
    client.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)
    print(f"Successfully downloaded {FILE_NAME}")
except Exception as e:
    print(f"Error downloading file: {e}")


