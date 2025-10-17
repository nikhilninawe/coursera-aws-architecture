import json, boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        if record["eventName"] == "INSERT":
            new_record = record["Dynamodb"]["NewImage"]
            response = client.publish(
                TopicArn='arn:aws:sns:ap-south-1:184897976500:POC-Topic:0fd158a6-0253-4fd3-93ed-4dfd0dda5c2e',
                Message=json.dumps({'default': json.dumps(new_record)}),
                MessageStructure='json'
            )