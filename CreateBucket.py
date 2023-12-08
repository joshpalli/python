import json
import boto3

def lambda_handler(event, context):
    # create an s3 client
    client = boto3.client('s3')
    
    # implement create bucket function
    reponse = client.create_bucket(
        Bucket='joshgithubbucket',
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2',
            
        },
    )