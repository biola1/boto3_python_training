import boto3
s3 =boto3.client('s3')
bucket='biola-boto-07082023'
key='test_texter_string.txt'
response = s3.get_object(Bucket=bucket, Key=key)
object_content = response['Body'].read()
contents = object_content.decode('utf-8')
print (contents)
