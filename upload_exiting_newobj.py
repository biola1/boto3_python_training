import boto3
s3 = boto3.client('s3')
s3.put_object(Bucket="biola-boto-07082023", Key="test_texter_string.txt", Body='This is another way of creaing object', ContentType='text/plain')
