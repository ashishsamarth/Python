def s3_list_buckets(self) -> list:
    '''
    Method to list S3 buckets on the user account
    Argument to this method is: None
    '''
    # Using List comprehension, pull the bucket names from the response of list_buckets method
    buckets = [_['Name'] for _ in self.s3_client.list_buckets()['Buckets']]
    # return type of this method is a list
    return buckets