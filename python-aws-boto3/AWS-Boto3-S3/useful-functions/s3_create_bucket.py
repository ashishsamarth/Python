def s3_create_bucket(self, _bucket_name):
    '''
    Method to create a S3 Bucket
    Argument to this method is:- Bucket Name
    Note: S3 bucket names must be globally unique amongst all AWS customers
    '''
    try:
        # Call the create_bucket method on the object
        execute = self.s3_client.create_bucket(Bucket=_bucket_name)
        if execute['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(str(_bucket_name) + ':- ' + 'created successfully')
    # In case code encounters common error, a brief message of the error will be presented to the user
    except ClientError as error_data:
        if error_data.response['Error']['Code'] in AwsBoto3S3.S3_Error_Map.keys():
            print(str(_bucket_name) + ':- ' + AwsBoto3S3.S3_Error_Map[error_data.response['Error']['Code']]) 