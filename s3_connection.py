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


def get_aws_session(credentials=CREDENTIALS):
    session = boto3.Session(
        aws_access_key_id=credentials["aws_access_key_id"],
        aws_secret_access_key=credentials["aws_secret_access_key"],
    )
    return session


def yield_items_in_bucket(bucket):
    """
    GENERATOR: Yields avalable obj metadata on each item in bucket
    """
    for obj in bucket.objects.all():
        d = {
            "key": obj.key,
            "last_modified": obj.last_modified,
            "meta": obj.meta,
            "owner": obj.owner,
            "size": obj.size,
        }

        yield d


session = get_aws_session(CREDENTIALS)
s3 = session.resource("s3")
bucket = s3.Bucket(RAW_IMAGES_BUCKET)
