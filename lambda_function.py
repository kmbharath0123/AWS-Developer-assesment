#python function to get data from SSM (parameter store and upload to s3 bucket)
# this function is working fine 
import boto3
import json 
import os

ssm = boto3.client('ssm' , region_name ='ap-southeast-1')
s3 = boto3.client('s3')


def lambda_handler(event, context):
    res = ssm.get_parameter(Name="Username")
    parameter_name = res['Parameter']['Name']
    parameter_value = res['Parameter']['Value']
    f=open("/tmp/data.txt",'w+')
    f.write(parameter_name + '\n')
    f.write(parameter_value)
    f.close()
    s3.upload_file('/tmp/data.txt', 'mytestvalues', 'data.txt')