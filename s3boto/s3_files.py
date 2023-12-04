import boto3
import gzip
from io import BytesIO

boto3.setup_default_session(profile_name='')
s3_client = boto3.resource('s3')

my_bucket = s3_client.Bucket('')

for file in my_bucket.objects.all():
    print(file.key)
    gzipped_content = file.get()['Body'].read()

    # Decompress the gzipped content
    decompressed_content = gzip.GzipFile(fileobj=BytesIO(gzipped_content)).read()

    # Print or process the decompressed content as plain text
    print(decompressed_content.decode('utf-8'))
    input("\n\n\n start next? \n")
