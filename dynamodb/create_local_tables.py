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

session = Session(**credentials)
client = session.client(**params)

existing_table_names = client.list_tables().get('TableNames', [])

table_name_schema_map = {
    TABLE_NAME: dict(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'pkey',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'skey',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'pkey',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'skey',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PROVISIONED',
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        }
    )
}

for table_name, schema in table_name_schema_map.items():
    if table_name not in existing_table_names:
        response = client.create_table(**schema)
        pprint(response)

    else:
        print(f'\nTable "{table_name}" already exists\n')
        pprint(client.describe_table(TableName=table_name))
