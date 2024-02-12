import os
import boto3
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def get_table():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.environ.get('ACCESS_KEY', ''),
                              aws_secret_access_key=os.environ.get('SECRET_KEY', ''),
                              region_name=os.environ.get('REGION', ''))

    table = dynamodb.Table(os.environ.get('TABLE_NAME', 'mcart-order-details'))
    return table


def get_logger():
    return LOG
