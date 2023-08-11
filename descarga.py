import boto3

s3 = boto3.client('s3')

nombre_bucket = 'bdjdv'

ruta_en_s3 = 'hola.txt'  

ruta_local = '/home/ubuntu/python_p/hola.txt'

s3.download_file(nombre_bucket, ruta_en_s3, ruta_local)
