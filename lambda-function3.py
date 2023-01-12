#function to copy a file from s3 bucket to a Dynamodb table
#importing packages
import json
import boto3
#function definition
def lambda_handler(event,context):
    
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('khalid-source-bucket')
    #table name
    table = dynamodb.Table('khalid-table')
    id=0
    for obj in bucket.objects.filter(Prefix='',Delimiter='/'):
        response = table.put_item(
        Item={
                'id':id,
                'Name': obj.key,
                
            }
        )
        id+=1
    return response