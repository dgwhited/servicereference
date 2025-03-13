import json
import os
import sys
import requests
from pathlib import Path

# URL to the service index
INDEX_URL = 'https://servicereference.us-east-1.amazonaws.com/v1/access-analyzer/access-analyzer.json'

def main():
    try:
        print(f"Fetching service index from {INDEX_URL}")
        response = requests.get(INDEX_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        services = response.json()
        
        if not isinstance(services, list):
            raise ValueError(f"Expected a list but got {type(services)}")
        
        print(f"Found {len(services)} services to process")
        
        # Process each service
        for service in services:
            if not service.get('service') or not service.get('url'):
                print(f"Skipping invalid service entry: {json.dumps(service)}")
                continue
            
            service_name = service['service']
            print(f"Processing service: {service_name}")
            
            # Create directory for the service
            service_dir = Path(service_name)
            service_dir.mkdir(exist_ok=True)
            
            # Fetch the service JSON
            try:
                service_response = requests.get(service['url'])
                service_response.raise_for_status()
                service_data = service_response.json()
                
                # Save the service data
                output_path = service_dir / f"{service_name}.json"
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(service_data, f, indent=2)
                print(f"Saved {service_name} data to {output_path}")
            except Exception as e:
                print(f"Error fetching data for {service_name}: {str(e)}")
        
        print("Service reference scraping completed successfully")
    except Exception as e:
        print(f"Error in main process: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
