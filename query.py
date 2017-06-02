import boto3
from boto3.dynamodb.conditions import Key, Attr
import yaml


# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Mldeploy')
# Create the DynamoDB table.
response = table.query(
    KeyConditionExpression=Key('ToHash').eq('X')
)
items = response['Items']
acc = float((items)[0]['acc'])
print acc

with open('data.yml', 'r') as outfile:
	data = yaml.load(outfile)

data['acc1'] = acc

with open('data.yml', 'w') as outfile:
	yaml.dump(data, outfile, default_flow_style=False)
