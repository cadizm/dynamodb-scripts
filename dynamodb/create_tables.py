from pprint import pprint

from config import TABLE_NAME
from config import client


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
        BillingMode='PAY_PER_REQUEST',
        # BillingMode='PROVISIONED',
        # ProvisionedThroughput={
        #     'ReadCapacityUnits': 100,
        #     'WriteCapacityUnits': 100
        # }
    )
}

for table_name, schema in table_name_schema_map.items():
    if table_name not in existing_table_names:
        response = client.create_table(**schema)
        pprint(response)

    else:
        print(f'\nTable "{table_name}" already exists\n')
        pprint(client.describe_table(TableName=table_name))
