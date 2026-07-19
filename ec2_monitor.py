import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

def monitor_ec2_health():
    print("Fetching EC2 instance status...\n")
    
    # Retrieve information for all instances
    response = ec2.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            
            # Retrieve the instance name from tags
            name = "Unnamed"
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
            
            print(f"Name: {name} | ID: {instance_id} | Status: {state}")

if __name__ == "__main__":
    monitor_ec2_health()