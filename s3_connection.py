import boto3
from boto.s3.connection import S3Connection
import configparser

def get_config_parser():
    # ConfigParser to read config.ini
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config

def get_S3_credentials():
    CredentialsConfig = get_config_parser()

    credentials = {
    'aws_access_key_id' : CredentialsConfig.get("aws_credentials", "aws_access_key_id"),
    'aws_secret_access_key' : CredentialsConfig.get("aws_credentials", "aws_secret_access_key"),
    'aws_session_token' : CredentialsConfig.get("aws_credentials", "aws_session_token"),
    'conn' : S3Connection(
                CredentialsConfig.get("aws_credentials", "aws_access_key_id"),
                CredentialsConfig.get("aws_credentials", "aws_secret_access_key")),
    'region' : 'us-east-1'
    }
    return credentials

def get_s3_client(credentials):
    credentials = get_S3_credentials()

    s3 = boto3.client(
        "s3",
        aws_access_key_id=credentials['aws_access_key_id'],
        aws_secret_access_key=credentials['aws_secret_access_key'],
        aws_session_token=credentials['aws_session_token'],
        region_name=credentials['region'],
    )
    return s3

def get_bucket(client, bucket_name):
    bucket = client.get_bucket(bucket_name)
    return bucket


S3_BUCKET = "shutiimgbucket"
CSV_FILE = "img_data.csv"
CREDENTIALS = get_S3_credentials()
s3 = get_s3_client(CREDENTIALS)
con = CREDENTIALS['conn']


def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys


s3_resource = boto3.resource('s3',
        aws_access_key_id=CREDENTIALS['aws_access_key_id'],
        aws_secret_access_key= CREDENTIALS['aws_secret_access_key'],
        aws_session_token= CREDENTIALS['aws_session_token'],
        )

# s3_resource = boto3.resource('s3',
#         aws_access_key_id=CREDENTIALS['aws_access_key_id'],
#         aws_secret_access_key= CREDENTIALS['aws_secret_access_key'])

# bucket = s3_resource.Bucket(S3_BUCKET)
# s3_resource.Object(S3_BUCKET, CSV_FILE).download_file(CSV_FILE)


#        region_name=CREDENTIALS['region'],

#s3.list_objects_v2(Bucket="eb6259dddf801e581271aaa026bba894a77281f2b9bd51ad9db622675b3a9e35")


bucket = s3_resource.Bucket("eb6259dddf801e581271aaa026bba894a77281f2b9bd51ad9db622675b3a9e35")
bucket = s3_resource.Bucket(S3_BUCKET)