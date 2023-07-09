import boto3
s3= boto3.client('s3')
bucket='cf-templates-fw95kij3puwj-us-east-1'
response = s3.delete_bucket(
    Bucket=bucket
)

print(response)