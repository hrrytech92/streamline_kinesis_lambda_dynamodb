import boto3
import json
import time
import random

kinesis = boto3.client('kinesis', region_name='us-east-2')

def generate_event():
    return {
        'user_id': random.randint(1, 100),
        'timestamp': time.time(),
        'event_type': random.choice(['click', 'view', 'purchase'])
    }

while True:
    data = json.dumps(generate_event())
    response = kinesis.put_record(
        StreamName='realtime-events-stream',
        Data=data,
        PartitionKey='partition-key'
    )

    print(f"resonse = {response}")
    time.sleep(1)