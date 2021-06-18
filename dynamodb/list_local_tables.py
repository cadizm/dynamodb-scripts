from pprint import pprint

from boto3.session import Session

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

pprint(client.list_tables().get('TableNames', []))
