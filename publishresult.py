import boto3
import os
from botocore.exceptions import ClientError
bucket = os.getenv('BUCKET_NAME')
aws_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
client = boto3.client(
    's3',
    aws_access_key_id=aws_key_id,
    aws_secret_access_key=aws_secret_access_key
)
build_number = os.getenv('CI_JOB_ID')
directory_name= 'surefire-reports-'+str(build_number)
directory_name_str=str("target/")+str(directory_name)+ str("/emailable-report.html")
file_name='emailable-report.html'
def upload_file(dir_name, bucket, file_name):
    s3_client = boto3.resource(
        's3',
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    folder=(directory_name+'/')
    try:
        response = s3_client.meta.client.upload_file(directory_name_str, bucket , directory_name_str,ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/html'})
        print(response)
    except ClientError as e:
        print(e)
        return False
    return True
upload_file(directory_name_str,bucket,file_name)