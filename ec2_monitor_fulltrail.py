import boto3
from datetime import datetime, timedelta

# Initialize clients
ec2 = boto3.client('ec2', region_name='us-east-1')
cloudtrail = boto3.client('cloudtrail', region_name='us-east-1')

def get_stop_reason(instance_id):
    # Search CloudTrail for the 'StopInstances' event
    response = cloudtrail.lookup_events(
        LookupAttributes=[{'AttributeKey': 'ResourceName', 'AttributeValue': instance_id}],
        StartTime=datetime.utcnow() - timedelta(days=7) # Look back 7 days
    )
    
    for event in response['Events']:
        if 'StopInstances' in event['EventName']:
            # Decode the user info from the event
            user = event.get('Username', 'Unknown User')
            return f"Stopped by: {user} at {event['EventTime']}"
    return "No stop event found in recent logs."

def monitor_ec2_health():
    print("Fetching EC2 instance status and audit logs...\n")
    
    response = ec2.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            name = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), "Unnamed")
            
            print(f"Name: {name} | ID: {instance_id} | Status: {state}")
            
            if state == 'stopped':
                reason = get_stop_reason(instance_id)
                print(f"   -> Root Cause: {reason}")
            print("-" * 50)

if __name__ == "__main__":
    monitor_ec2_health()