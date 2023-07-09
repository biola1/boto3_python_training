import boto3
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket='biola-boto-07082023')

for content in response['Contents']:







    if('.txt' in content['Key']):
        print(content['Key'])