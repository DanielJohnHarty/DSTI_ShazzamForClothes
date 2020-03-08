import boto3
import auxiliary_functions as aux


def get_S3_credentials():

    config_parser = aux.CONFIG_PARSER

    credentials = {
        "aws_access_key_id": config_parser.get("aws_credentials", "aws_access_key_id"),
        "aws_secret_access_key": config_parser.get(
            "aws_credentials", "aws_secret_access_key"
        ),
        "region": config_parser.get("aws_global_parameters", "target_region"),
    }
    return credentials


RAW_IMAGES_BUCKET = aux.CONFIG_PARSER.get("aws_s3_parameters", "raw_images_bucket_name")
CSV_FILE = aux.CONFIG_PARSER.get("aws_s3_parameters", "related_data_csv")
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