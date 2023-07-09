import boto3
s3 = boto3.client('s3')

bucket='biola-boto-07082023'
key=  'test_texter.txt'
filename= 'test_texter.txt'
def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename )