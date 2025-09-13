import boto3

class SimpleS3():
        def __init__(self,region="us-east-1"):
                self.region = region
                self.client = boto3.client("s3")

        def create_bucket(self,name):
                self.client.create_bucket(Bucket=name,
                        CreateBucketConfiguration={'LocationConstraint':self.region})
                print(f"Bucket {name} created successfully.")

        def list_objects(self,bucket):
                response = self.client.list_objects_v2(Bucket=bucket)
                n = 0
                for item in response['Contents']:
                        n = n + 1
                        print(f"{n}. {item['Key']}")
                print(f"Total objects in S3 Bucket: {n}")

        def upload_file(self,bucket,file_path,key=None):
                key = file_path
                self.client.upload_file(file_path,bucket,key)
                print(f"{file_path} -----> s3://{bucket}/{key}")
