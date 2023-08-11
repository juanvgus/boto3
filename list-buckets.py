import boto3 

client = boto3.client('s3', 'us-east-1')

#print(client.list_buckets())

data_buckets = client.list_buckets()

for element in data_buckets['Buckets']:
    print(element['Name'])
♠
