import boto3
s3=boto3.client('s3')
response = s3.generate_presigned_url('get_object', Params={'Bucket': "biola-boto-07082023", 'Key': "test_texter.txt"},ExpiresIn=300)
print(response)