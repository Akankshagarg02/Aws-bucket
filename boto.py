

import boto3
s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print (bucket.name)


#s3.create_bucket(Bucket='mybucket38')
#s3.Object('mybucket38','hello.txt').put(Body=open())

#s3.Object('mybucket38', 'hello.txt').put(Body=open('/home/akanksha/software/hello.txt', 'rb'))
#s3.Object('mybucket38', 'pycharm-4.0.1.zip').put(Body=open('/home/akanksha/software/pycharm-4.0.1.zip', 'rb'))
#s3.Object('mybucket38', 'image-slider-2.jpg').put(Body=open('/home/akanksha/Documents/image-slider-2.jpg', 'rb'))

searchBucket = raw_input("Enter bucket name to be search:")
#print(type(searchBucket))
def bucket_search(searchBucket):
    for bucket in s3.buckets.all():
        #print (bucket.name)
        if bucket.name == searchBucket:
            print("bucket exists")
            return True
    print("bucket does not exist")
    return False

def object_list_bucket(searchBucket):
    obj_list=[]
    bucket = s3.Bucket(searchBucket)
    for obj in bucket.objects.all():
        obj_list.append(obj)
    return obj_list

if bucket_search(searchBucket):
    obj_list = object_list_bucket(searchBucket)
    for obj in obj_list:
        print (obj.key)
else:
    print ("Try with another Bucket name")






# import botocore
# bucket = s3.Bucket('mybucket38')
# exists = True
# try:
#     s3.meta.client.head_bucket(Bucket='mybucket3')
# except botocore.exceptions.ClientError as e:
#     # If a client error is thrown, then check that it was a 404 error.
#     # If it was a 404 error, then the bucket does not exist.
#     error_code = int(e.response['Error']['Code'])
#     if error_code == 404:
#         exists = False
# print(exists)


# def bucket_search1(desired_bucket, start=0, end=None):
#     buckets = list(s3.buckets.all())
#     if end is None:
#         end = len(buckets)
#
#     if start == end:
#         #raise ValueError("%s was not found in the list." % desired_bucket)
#         print("bucket is not present")
#
#     pos = (end - start) // 2 + start
#
#     if desired_bucket == buckets[pos].name:
#         return pos
#     elif desired_bucket > buckets[pos].name:
#         return bucket_search1(desired_bucket, start=(pos + 1), end=end)
#     else:
#         return bucket_search1(desired_bucket, start=start, end=pos)
#
# bucket_search1(searchBucket)


