
"""
    PoC for managing EC2 instance from Pythons scripts
    for more: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
"""

import boto3

ec2_client = boto3.client('ec2')
ec2r_resource = boto3.resource('ec2')

def getAllInstances():
    """ Get all instances """
    response = ec2_client.describe_instances()
    return response['Reservations']


def getInstance(instanceId=None):
    """ Get specific instance """
    if instanceId is not None:
        return ec2r_resource.Instance(instanceId)

def myToString(instance):
    """ Prints several attributes of an instance"""
    attrs = ['id','cpu_options','architecture','instance_type','public_ip_address','state','image']
    [print((i,getattr(instance,i))) for i in attrs ]


if __name__ == '__main__':
    getAllInstances()