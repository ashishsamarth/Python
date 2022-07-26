import boto3
from botocore.exceptions import ClientError

class AwsBoto3S3:

    AWS_REGION = {'loc_1': 'us-east-1'}

    S3_Error_Map = {'InvalidBucketName': 'BucketName does not align with S3 naming convention',
                    'BucketAlreadyExists': 'The requested bucket name is not available.',
                    'IllegalLocationConstraintException': 'The unspecified location constraint is incompatible for the region',
                    'NoSuchBucket': 'The specified bucket does not exist'}
    
    def __init__(self):
        # initialize the class with a variable s3_client & s3_resource
        # region_name will hold the region name you want to work with as a part of initialization
        self.s3_client = boto3.client('s3', region_name=AwsBoto3S3.AWS_REGION['loc_1'])
        self.s3_resource = boto3.resource('s3', region_name=AwsBoto3S3.AWS_REGION['loc_1'])
    
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
