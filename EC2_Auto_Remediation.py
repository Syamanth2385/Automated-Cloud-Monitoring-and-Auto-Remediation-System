import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = 'i-xxxxxxxxxxxxxxxxx'  # replace with your instance ID

def lambda_handler(event, context):
    """
    Auto-remediation Lambda function.
    Reboots EC2 instance when triggered by CloudWatch alarm via SNS.
    """
    ec2.reboot_instances(InstanceIds=[INSTANCE_ID])
    print(f"Rebooted EC2 instance {INSTANCE_ID}")
