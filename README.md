# 💾 Smart Data Backup System using AWS S3 & Python

## 📘 Overview

This project is a smart and automated data backup system designed to securely upload files from a specified directory to an AWS S3 bucket and validate the backup using hash-based file integrity checks. It leverages the power of Python, Boto3, and Amazon S3, offering a scalable and configuration-driven solution for backing up critical files.

---

## 🎯 Objective

Manual backups are error-prone and time-consuming. This project automates the process of:
- Uploading files from a local folder to an S3 bucket
- Ensuring file integrity post-upload using MD5 hash comparison
- Centralizing backup configurations using a .properties file

---

# 🛠️ Tools & Technologies

- **Programming**:	Python
- **Cloud Platform**:	AWS S3
- **SDK**:	Boto3
- **Config Management**:	configparser & .properties file
- **Security**:	Hashlib (for MD5 validation)

---

# 📁 Repository Structure

- ├── main.py               # Main script that triggers backup and integrity check
- ├── uploadtoS3.py         # Core logic for uploading files to S3 and verifying hashes
- ├── config.properties     # Config file for AWS keys, region, and S3 bucket name
- ├── README.md             # Project documentation

---

# 🔄 How It Works

### 1. Configure Settings
Update the config.properties file with:
- AWS Access & Secret Keys
- S3 Bucket Name
- AWS Region

### 2. Backup Process
Run the main.py script:
- Recursively uploads all files from the target directory to S3
- Stores a hash of each file before upload
- Compares the hash of the uploaded file to ensure integrity

### 3. Output
- Console messages for upload status
- Success/failure alerts for each file’s integrity check

---

## ✅ Features

- 🔒 Secure Backups: Upload files directly to your AWS S3 bucket
- 🔁 Automated Integrity Check: Ensures each file uploaded matches its source
- 🧠 Smart Configuration: Adjust bucket/region without modifying source code
- 📦 Zip-ready Deployment: Package as a .zip for use in other automation tasks or cron jobs

---

## 📈 Potential Enhancements

- Add email notifications after successful backup
- Enable incremental or scheduled backups using cron
- Integrate with AWS SNS for alerts
- Store hash values in DynamoDB for long-term audit trail

