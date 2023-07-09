import boto3
from list_object2 import list-bucket-v2
s3=boto3.client('s3')


def delete_object(client,bucket,key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key,
    )
    return response

def delete_objects(client,bucket,keys):
    objects = [{'Key': key} for key in keys]
    response = client.delete_objects(
            Bucket=bucket,
            Delete={
            'Objects': objects
        }
    )
    return response
bucket='biola-boto-07082023'
key='test_texter.txt'
response = s3.delete_object(
    Bucket=bucket,
    Key=key,
  
)


    
keys =['test_texter_new.txt', 'test_texter_string.txt']
delete_objects(s3,bucket,keys)
list_object_keys(client, bucket, prefix='New Folder/')