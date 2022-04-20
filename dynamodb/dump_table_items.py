from pprint import pprint

from config import TABLE_NAME
from config import client, dynamodb


table_name_attribute_map = {
    TABLE_NAME: dict(
        partition_key_name='pkey',
        sort_key_name='skey',
        ttl_key='ttl'
    )
}

existing_table_names = client.list_tables().get('TableNames', [])

for table_name, attribute_map in table_name_attribute_map.items():
    table = dynamodb.Table(table_name)

    if table_name in existing_table_names:
        print(f'\nTable {table_name}\n')
        pprint(table.scan(AttributesToGet=list(attribute_map.values())))
    else:
        print(f'Table "{table_name}" does not exist\n')
