import json
import boto3
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProcessedEvents')

def lambda_handler(event, context):
    print("Lambda function was called!")

    for record in event['Records']:
        payload = json.loads(base64.b64decode(record['kinesis']['data']).decode('utf-8'))
        
        response = table.put_item(Item={
            'user_id': str(payload['user_id']),
            'timestamp': str(payload['timestamp']),
            'event_type': payload['event_type']
        })
        
        print("PutItem response:", response)

    return {'status': 'success'}
