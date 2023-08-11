import boto3 

data_client =  boto3.client('s3', 'us-east-1')
data = data_client.list_objects_v2(Bucket='bdjdv')

#print(data)

for obj in data['Contents']:
	print(obj['Key'])
