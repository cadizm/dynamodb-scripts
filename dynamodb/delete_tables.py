from pprint import pprint

from config import TABLE_NAME
from config import client


existing_table_names = client.list_tables().get('TableNames', [])

for table_name in [TABLE_NAME]:
    if table_name in existing_table_names:
        pprint(client.delete_table(TableName=table_name))

    else:
        print(f'\nTable "{table_name}" does not exist\n')
