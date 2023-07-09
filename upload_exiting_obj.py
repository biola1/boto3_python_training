import boto3
s3 = boto3.client('s3')
with open("test_texter.txt", 'rb') as f:
    s3.put_object(Bucket="biola-boto-07082023", Key="test_texter.txt", Body=f, ContentType='text/plain')
