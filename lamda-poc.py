import boto3, uuid

client = boto3.resource('dynamodb')
table = client.Table('orders')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        print(payload)
        table.put_item(
            Item={
                'orderID': str(uuid.uuid4()),
                'payload': payload
            }
        )