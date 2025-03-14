# AWS Service Reference

This repository contains automatically scraped AWS service reference data from https://servicereference.us-east-1.amazonaws.com in JSON format.


## Repository Structure

Each AWS service has its own directory containing a JSON file with the service's reference data:

```
├── ec2
│ └── ec2.json
├── s3
│ └── s3.json
├── lambda
│ └── lambda.json
└── ...
```

## Data Updates

The service reference data is automatically updated every 8 hours via a GitHub Actions workflow. When changes are detected, a new release is created with a changelog detailing the modifications.
