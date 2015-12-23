import boto3
session = boto3.session.Session(aws_access_key_id='AKIAIE77JWLUJPBLUBMA',
                  aws_secret_access_key='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',
                  region_name='ap-southeast-1')
s3_client = session.client('s3')
s3_client.upload_file('data.json', 'tamilrockersdump', 'data.json')