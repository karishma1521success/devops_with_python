import boto3

# client is used to talk with aws api
# boto3 has two methods to talk with aws api 
# 1. client        2. resource (don't work in new services)
client = boto3.client('s3')

response = client.create_bucket(
    Bucket='my-first-bucket-using-boto3',  #provide bucket name (required field)
)

# this code will create s3 bucket