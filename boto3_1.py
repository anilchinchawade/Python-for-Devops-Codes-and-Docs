#API Demo
import requests 
import boto3

client = boto3.client("s3")
# response = client.create_bucket(    
#     Bucket='anil-boto-bucket-1-create-demo'    
# )


response = client.get_bucket_acl(
    Bucket='anil-boto-bucket-1-create-demo'
)

print(response)
# for key in response:
#     print(key)