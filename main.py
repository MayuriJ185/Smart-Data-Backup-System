import os
import boto3
import hashlib,configparser
import smtplib
from botocore.exceptions import NoCredentialsError
from source.uploadtoS3 import upload_files_to_s3
from llm_summary import generate_backup_summary

def main():
    backup_dir = r"C:\Users\maayu\OneDrive\Pictures\Test folder"
    print("Starting backup process...")
    # Step 1: Upload files to S3
    file_hashes = upload_files_to_s3(backup_dir)

    # Step 2: Verify file integrity
    failed_files = []
    for filename, file_hash in file_hashes.items():
        if not verify_backup_integrity({filename: file_hash}):
            failed_files.append(filename)
    
    # Step 3: Capture backup summary
    summary = {
    "total_files": len(file_hashes),
    "failed_integrity": failed_files,
    "successful_uploads": len(file_hashes) - len(failed_files),
    "directory": backup_dir
}

summary_message = generate_backup_summary(summary)
print("SMART NOTIFICATION:", summary_message)

if __name__ == "__main__":
    main()
