"""Manage s3 bucket"""

import boto3

session = boto3.session.Session(profile_name='personal')
client_s3 = session.resource('s3')

def getAllS3():
    """Get all buckets"""
    for bucket in client_s3.buckets.all():
      print(bucket.name)

def getBucket(name=None):
    return client_s3.Bucket(name)

def readHardFile():
    with open('https://general-use-andres.s3.amazonaws.com/hello.txt', 'r') as data:
        print (data)

if __name__ == '__main__':
    #getBucket(name='general-use-user').download_file('hello.txt', r'hello.txt')
    getAllS3()
    #readHardFile()
    pass