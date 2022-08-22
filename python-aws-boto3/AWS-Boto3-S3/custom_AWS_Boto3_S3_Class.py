import boto3
from botocore.exceptions import ClientError

class AwsBoto3S3:

    AWS_REGION = {'loc_1': 'us-east-1'}

    S3_Error_Map = {'InvalidBucketName': 'BucketName does not align with S3 naming convention',
                    'BucketAlreadyExists': 'The requested bucket name is not available.',
                    'IllegalLocationConstraintException': 'The unspecified location constraint is incompatible for the region',
                    'NoSuchBucket': 'The specified bucket does not exist'}
    
    def __init__(self):
        ''' 
        initialize the class with a variable s3_client & s3_resource
        region_name will hold the region name you want to work with as a part of initialization 
         '''
        self.s3_client = boto3.client('s3', region_name=AwsBoto3S3.AWS_REGION['loc_1'])
        self.s3_resource = boto3.resource('s3', region_name=AwsBoto3S3.AWS_REGION['loc_1'])
    
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

    def s3_list_buckets(self):
        '''
        Method to list S3 buckets on the user account
        Argument to this method is: None
        '''
        # Using List comprehension, pull the bucket names from the response of list_buckets method
        buckets = [_['Name'] for _ in self.s3_client.list_buckets()['Buckets']]
        # return type of this method is a list
        return buckets

    # Method to delete empty bucket
    # Argument to this method is:- Bucket Name
    def s3_delete_empty_bucket(self, _bucket_name):
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

    # Method to copy file from one data bucket to another
    # Arguments to this method are:- Source-Bucket-Name, Source-File-Name, Target-Bucket-Name, Target-File-Name
    def s3_bucket_copy_file_from_one_bucket_to_another(self, _src_bucket_name, _src_file_name, _tgt_bucket_name, _tgt_file_name):
        # Special Note: We have to use s3_resource instead of s3_client
        # capture the source bucket name and source file name in 'copy_source'
        # copy_source should not be modified, since its part of syntax
        copy_source = {'Bucket': _src_bucket_name, 'Key': _src_file_name}
        # s3_resource.meta.client.copy is the core of this method
        self.s3_resource.meta.client.copy(copy_source, _tgt_bucket_name, _tgt_file_name)
        return 'File Copied to Target S3 Bucket'

    # Method to delete specific file from a given S3 bucket
    # Arguments to this method are:- Bucket-Name and File-Name to be deleted
    def s3_bucket_delete_specific_file(self, _bucket_name, _file_name):
        try:
            # Pull the objects in the specified bucket in to a variable (return type is a dictionary)
            item = self.s3_client.list_objects(Bucket=_bucket_name)
            # Get the list of files names into 'file_list' using list comprehension
            file_list = [_['Key'] for _ in item['Contents']]
            if _file_name in file_list:
                # proceed with calling the 'delete_objects' method on the S3 object
                self.s3_client.delete_object(Bucket=_bucket_name, Key=_file_name)
                # Print the following method on the terminal
                return f'\'{_file_name}\' deleted from \'{_bucket_name}\' successfully'
            else:
                return f'\'{_file_name}\' --NOT FOUND-- in \'{_bucket_name}\' bucket. Please check the file name for typo(s)...'
        # In case code encounters common error, a brief message of the error will be presented to the user
        except ClientError as error_data:
            if error_data.response['Error']['Code'] in AwsBoto3S3.S3_Error_Map.keys():
                print(str(_bucket_name) + ':- ' + AwsBoto3S3.S3_Error_Map[error_data.response['Error']['Code']])        
