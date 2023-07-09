import boto3
s3 = boto3.client('s3')
s3.upload_file('test_texter.txt', 'biola-boto-07082023', 'test_texter_new.txt', ExtraArgs= {'ContentType': 'text/plain'})
