import os
import boto3
from ShazzamForClothes.config import LOADED_CONFIG

__all__ = [
    "get_S3_credentials",
    "get_aws_session",
    "yield_items_in_bucket",
    "download_file_from_bucket",
    "get_s3_resource",
    "get_s3_bucket",
    "get_aws_session"
]


def get_S3_credentials(config_parser=LOADED_CONFIG):

    credentials = {
        "aws_access_key_id": config_parser.get("aws_credentials", "aws_access_key_id"),
        "aws_secret_access_key": config_parser.get(
            "aws_credentials", "aws_secret_access_key"
        ),
        "region": config_parser.get("aws_global_parameters", "target_region"),
    }
    return credentials


RAW_IMAGES_BUCKET = LOADED_CONFIG.get("aws_s3_parameters", "raw_images_bucket_name")
CSV_FILE = LOADED_CONFIG.get("aws_s3_parameters", "related_data_csv")
CREDENTIALS = get_S3_credentials()


def get_s3_resource(credentials=CREDENTIALS):
    session = get_aws_session(credientials)
    s3 = session.resource("s3")
    return s3


def get_s3_bucket(s3_resource, bucket_name=RAW_IMAGES_BUCKET):
    bucket = s3_resource.Bucket(bucket_name)
    return bucket


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


def download_file_from_bucket(
    target_filename, s3_bucket=RAW_IMAGES_BUCKET, local_directory=""
):
    try:
        download_path = os.path.join(local_directory, target_filename)
        s3_bucket.download_file(target_filename, download_path)
    except Exception as e:
        raise Exception(e)

