
""" PoC for managing EC2 instance from Pythons scripts """

import boto3

ec2 = boto3.client('ec2')

""" Get all instances """
response = ec2.describe_instances()
print(response)

""" Get specific instance """