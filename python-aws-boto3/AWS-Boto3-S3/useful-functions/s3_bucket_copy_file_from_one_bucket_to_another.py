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
