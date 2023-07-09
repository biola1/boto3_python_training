import boto3
def filter_objects_extension(client, extension):
    keys:[]
    response = s3.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if(extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
    return keys
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket='biola-boto-07082023')
for content in response['Contents']:
    if(extension in content['Key'][-(len(extension)):]):
      keys.append(content['Key'])
response = filter_objects_extension(s3, bucket, '.txt')
extension = '.txt'
for content in response['Contents']:
    if(extension in content['Key']):
        print(content['Key'])
response = filter_objects_extension(s3, 'biola-boto-07082023', '.txt')
print(response)
