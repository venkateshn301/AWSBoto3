import boto3

#Accessing list of buckets from S3 bucket

s3client = boto3.client('s3')
print(s3client.getobject())