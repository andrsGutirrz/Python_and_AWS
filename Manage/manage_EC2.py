"""
    In this file, you can
    {
        create, delete,
        stop, start
    }
    an EC2 instance
"""
import boto3
from Query import query_EC2 as query


def createInstance(ami=None,type='t2.micro'):
    """
    Creates an EC2 instance
    :param ami: image id
    :return: None
    """
    if ami is not None:
        _ec2 = boto3.resource('ec2')
        instances = _ec2.create_instances(
            ImageId= ami,
            MinCount=1,
            MaxCount=1,
            InstanceType=type,
            KeyName='general-use-windows-personal'
        )
    else:
        print("No ami given")

def terminateInstance(instanceId=None):
    """Terminates the instance given by parameter"""
    if instanceId is not None:
        try:
            query.getInstance(instanceId).terminate()
        except Exception:
            print('Error handling instance id')
    else:
        print("No instanceId given")

def stopInstance(instanceId=None):
    """Stops the instance given by parameter"""
    if instanceId is not None:
        try:
            query.getInstance(instanceId).stop()
        except Exception:
            print('Error handling instance id')
    else:
        print("No instanceId given")

def startInstance(instanceId=None):
    """Stops the instance given by parameter"""
    if instanceId is not None:
        try:
            query.getInstance(instanceId).start()
        except Exception:
            print('Error handling instance id')
    else:
        print("No instanceId given")

def actionInstance(instanceId,action='stop'):
    """
    Performs actions to a singular instance
    :param instanceId: instance id
    :param action: action you want to perform: str {'terminate','stop','start'}
    :return: None
    """
    if instanceId is not None:
        try:
            #Calls action method
            getattr(query.getInstance(instanceId), action)()
        except Exception:
            print('Error handling instance id')
    else:
        print("No instanceId given")

if __name__ == '__main__':
    """Create instance"""
    #createInstance('ami-0a9ca0496f746e6e0')
    """Delete instance"""
    #terminateInstance('i-07b5ec0962ffaad0c')
    """Stop instance"""
    #stopInstance('i-05ded5ea6de50a579')
    """Start instance"""
    #startInstance('i-05ded5ea6de50a579')
    """Stop using generic function"""
    actionInstance('i-05ded5ea6de50a579','start')
    pass