from pprint import pprint

from boto3.session import Session

from config import *

# Don't need real credentials for local dynamodb
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
credentials = dict(
    aws_access_key_id='fake-key',
    aws_secret_access_key='fake-secret-key',
    aws_session_token='fake-token'
)

params = dict(
    service_name='dynamodb',
    region_name='us-west-2',
    endpoint_url='http://localhost:8000'
)

table_name_attribute_map = {
    TABLE_NAME: dict(
        partition_key_name='pkey',
        sort_key_name='skey',
        ttl_key='ttl'
    )
}

session = Session(**credentials)
client = session.client(**params)
dynamodb = session.resource(**params)

existing_table_names = client.list_tables().get('TableNames', [])

for table_name, attribute_map in table_name_attribute_map.items():
    table = dynamodb.Table(table_name)

    if table_name in existing_table_names:
        print(f'\nTable {table_name}\n')
        pprint(table.scan(AttributesToGet=list(attribute_map.values())))
    else:
        print(f'Table "{table_name}" does not exist\n')
