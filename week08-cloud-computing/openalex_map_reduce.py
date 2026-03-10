#!/usr/bin/env python

import os
import boto3
import json
import pandas as pd
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

def map_work(work):
    """
    MAP STEP: Extract specific metadata from a single OpenAlex work record.
    """
    # Extract primary topic if it exists
    primary_topic = work.get('primary_topic')
    topic_name = primary_topic.get('display_name') if primary_topic else "Unknown"
    
    return {
        'id': work.get('id'),
        'title': work.get('display_name'),
        'year': work.get('publication_year'),
        'citations': work.get('cited_by_count', 0),
        'topic': topic_name
    }

def reduce_results(mapped_data):
    """
    REDUCE STEP: Aggregate the extracted metadata into a summary report.
    """
    df = pd.DataFrame(mapped_data)
    
    summary = {
        'total_records': len(mapped_data),
        'average_citations': float(df['citations'].mean()),
        'most_cited_work': df.loc[df['citations'].idxmax()].to_dict(),
        'works_per_year': df.groupby('year').size().to_dict(),
        'top_topics': df['topic'].value_counts().head(5).to_dict()
    }
    return summary

def main():
    if not ACCESS_KEY or not SECRET_KEY:
        print("Error: DO_SPACES_KEY and DO_SPACES_SECRET must be set in .env")
        return

    # Take prefix as argument (e.g., group1/)
    prefix = sys.argv[1] if len(sys.argv) > 1
    if prefix != '' and not prefix.endswith('/'):
        prefix += '/'

    print(f"Starting OpenAlex Map-Reduce for S3 prefix: '{prefix}'")
    
    s3 = get_s3_client()
    all_mapped_records = []

    try:
        # List objects in the prefix
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)
        
        if 'Contents' not in response:
            print(f"No records found in {prefix}")
            return

        for obj in response['Contents']:
            key = obj['Key']
            if not key.endswith('.json'):
                continue
            
            # Fetch and Map Step
            print(f"  Mapping {key}...")
            obj_data = s3.get_object(Bucket=BUCKET_NAME, Key=key)
            work = json.loads(obj_data['Body'].read().decode('utf-8'))
            
            mapped_record = map_work(work)
            all_mapped_records.append(mapped_record)
            
        if all_mapped_records:
            # Reduce Step
            print("\nReducing all records...")
            final_summary = reduce_results(all_mapped_records)
            
            # Save the summary locally
            output_file = f'openalex_summary_{prefix.strip("/")}.json'
            with open(output_file, 'w') as f:
                json.dump(final_summary, f, indent=4)
                
            print(f"\nSummary generated and saved to {output_file}")
            print("-" * 30)
            print(f"Total Works: {final_summary['total_records']}")
            print(f"Avg Citations: {final_summary['average_citations']:.2f}")
            print(f"Top Topic: {list(final_summary['top_topics'].keys())[0]}")
        else:
            print("No JSON records to process.")

    except Exception as e:
        print(f"Error during Map-Reduce: {e}")

if __name__ == "__main__":
    main()
