def s3_delete_empty_bucket(self, _bucket_name):
    '''
    Method to delete empty bucket
    Argument to this method is:- Bucket Name
    '''
    try:
        # Pull the objects in the specified bucket in to a variable (return type is a dictionary)
        item = self.s3_client.list_objects(Bucket=_bucket_name)
        # Special Note:- If a bucket contains any kind of files / folders
        # Then 'Contents' will be one of the keys in the item (dictionary)
        # If the bucket is empty, then Key='Contents' will not exist in the response (item) dictionary
        # Following line validates, if the bucket is empty
        if 'Contents' not in item:
            # proceed with calling the 'delete_objects' method on the S3 object
            self.s3_client.delete_bucket(Bucket=_bucket_name)
            # Print the following method on the terminal
            print(str(_bucket_name) + ':- ' + 'was deleted successfully')
    # In case code encounters common error, a brief message of the error will be presented to the user
    except ClientError as error_data:
        if error_data.response['Error']['Code'] in AwsBoto3S3.S3_Error_Map.keys():
            print(str(_bucket_name) + ':- ' + AwsBoto3S3.S3_Error_Map[error_data.response['Error']['Code']])