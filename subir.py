import boto3

s3 = boto3.client('s3')

archivo_local = '/home/ubuntu/python_p/file.txt'

nombre_bucket = 'bdjdv'

ruta_en_s3 = 'file.txt'  

s3.upload_file(archivo_local, nombre_bucket, ruta_en_s3)


