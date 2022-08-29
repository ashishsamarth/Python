def s3_bucket_copy_file_from_one_bucket_to_another(self, _src_bucket_name: str, _src_file_name, _tgt_bucket_name, _tgt_file_name):
    '''
    Method to copy file from one data bucket to another
    Arguments to this method are:- Source-Bucket-Name, Source-File-Name, Target-Bucket-Name, Target-File-Name
    '''
    # Special Note: We have to use s3_resource instead of s3_client
    # capture the source bucket name and source file name in 'copy_source'
    # copy_source should not be modified, since its part of syntax
    copy_source = {'Bucket': _src_bucket_name, 'Key': _src_file_name}
    # s3_resource.meta.client.copy is the core of this method
    self.s3_resource.meta.client.copy(copy_source, _tgt_bucket_name, _tgt_file_name)
    return 'File Copied to Target S3 Bucket'
