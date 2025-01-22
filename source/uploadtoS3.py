import os
import boto3
import hashlib,configparser
import smtplib

def upload_files_to_s3(directory):
    root = os.getcwd()
    config = configparser.ConfigParser()
    configProperties = os.path.join(root, "config.properties")
    config.read(configProperties)
    s3_bucket_name = config.get('DEFAULT', 's3_bucket_name')
    aws_access_key = config.get('DEFAULT', 'aws_access_key')
    aws_secret_key = config.get('DEFAULT', 'aws_secret_key')
    region_name = config.get('DEFAULT', 'region_name')
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )
    file_hashes = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as file:
                # Calculate file hash
                file_hash = hashlib.md5(file.read()).hexdigest()
                file.seek(0)  # Reset file pointer after reading for hash

                try:
                    # Upload file to S3
                    s3.upload_fileobj(file, s3_bucket_name, filename)
                    print(f"Uploaded {filename} successfully.")
                    file_hashes[filename] = file_hash
                except NoCredentialsError:
                    print("AWS credentials not available.")

    return file_hashes

def verify_backup_integrity(file_hashes):
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )

    for filename, original_hash in file_hashes.items():
        try:
            s3_object = s3.get_object(Bucket=s3_bucket_name, Key=filename)
            downloaded_data = s3_object['Body'].read()
            downloaded_hash = hashlib.md5(downloaded_data).hexdigest()

            if downloaded_hash == original_hash:
                print(f"Integrity check passed for {filename}.")
            else:
                print(f"Integrity check failed for {filename}.")
        except Exception as e:
            print(f"Failed to verify {filename}: {e}")

