# S3 Cross-Account Migration Guide (Niwas → Mobicule)

## Overview

This document provides a complete production-safe step-by-step guide to
migrate an S3 bucket from the Niwas AWS account to the Mobicule AWS
account.

------------------------------------------------------------------------

# PHASE 1 --- PREPARATION

## Step 1 --- Collect Source Bucket Details (Niwas Account)

Login to AWS → S3 → Select Source Bucket

Collect the following details:

-   Bucket Name                          -          niwashfcprod-s3
-   Region                               -          Asia Pacific (Mumbai) ap-south-1
-   Versioning Status                    -          Enabled
-   Encryption Type (SSE-S3 or KMS)      -          Server-side encryption with AWS Key Management Service keys (SSE-KMS)
-   Total Bucket Size                    -          
-   Object Count

Document everything before proceeding.

------------------------------------------------------------------------

# PHASE 2 --- CREATE DESTINATION SETUP (Mobicule Account)

## Step 2 --- Create Destination Bucket

Login to Mobicule AWS account.

Go to S3 → Create Bucket

Recommendations: - Use same region as source (recommended) - Enable
Versioning - Enable Default Encryption (SSE-S3 recommended) - Keep
public access blocked unless required

Example bucket name: niwashfcprod-s3-migration-temp

------------------------------------------------------------------------

## Step 3 --- Create IAM User in Mobicule Account

Go to IAM → Users → Create User

Username: s3-migration-user

Enable: - Programmatic Access

Attach this policy (replace bucket name):

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowMobiculeReadAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::MOBICULE_ACCOUNT_ID:user/s3-migration-user"
      },
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::source-bucket-name",
        "arn:aws:s3:::source-bucket-name/*"
      ]
    }
  ]
}

Save: - Access Key - Secret Key

------------------------------------------------------------------------

# PHASE 3 --- ALLOW CROSS-ACCOUNT ACCESS (Niwas)

## Step 4 --- Add Bucket Policy in Niwas Account

Go to S3 → Source Bucket → Permissions → Bucket Policy

Add:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowMobiculeReadAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::MOBICULE_ACCOUNT_ID:user/s3-migration-user"
      },
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::source-bucket-name",
        "arn:aws:s3:::source-bucket-name/*"
      ]
    }
  ]
}

Replace: - MOBICULE_ACCOUNT_ID - source-bucket-name

------------------------------------------------------------------------

# PHASE 4 --- CONFIGURE MIGRATION SERVER

## Step 5 --- Install AWS CLI

On migration server:

For Amazon Linux: sudo yum install awscli -y

For Ubuntu: sudo apt install awscli -y

Verify: aws --version

------------------------------------------------------------------------

## Step 6 --- Configure AWS CLI Profiles

Configure Niwas profile: aws configure --profile niwas

Configure Mobicule profile: aws configure --profile mobicule

Verify: aws configure list-profiles

------------------------------------------------------------------------

# PHASE 5 --- TEST ACCESS

## Step 7 --- Test Source Access

aws s3 ls s3://source-bucket-name --profile niwas

## Step 8 --- Test Destination Access

aws s3 ls s3://niwas-prod-migrated --profile mobicule

------------------------------------------------------------------------

# PHASE 6 --- PRODUCTION SAFE MIGRATION

## Step 9 --- Dry Run (No Data Moved)

aws s3 sync s3://source-bucket-name s3://niwas-prod-migrated --profile
niwas --dryrun

------------------------------------------------------------------------

## Step 10 --- First Full Sync (No Downtime)

aws s3 sync s3://source-bucket-name s3://niwas-prod-migrated --profile
niwas --acl bucket-owner-full-control

Do NOT use --delete in first run.

------------------------------------------------------------------------

## Step 11 --- Validate Data

Compare object count: aws s3 ls s3://source-bucket-name --recursive
--profile niwas \| wc -l aws s3 ls s3://niwas-prod-migrated --recursive
--profile mobicule \| wc -l

Compare size: aws s3 ls s3://source-bucket-name --recursive --summarize
--profile niwas aws s3 ls s3://niwas-prod-migrated --recursive
--summarize --profile mobicule

------------------------------------------------------------------------

# PHASE 7 --- FINAL CUTOVER

## Step 12 --- Freeze Writes

-   Stop application uploads
-   Stop cron jobs
-   Enable maintenance mode

------------------------------------------------------------------------

## Step 13 --- Final Delta Sync

aws s3 sync s3://source-bucket-name s3://niwas-prod-migrated --profile
niwas --delete --acl bucket-owner-full-control

------------------------------------------------------------------------

## Step 14 --- Update Application Configuration

-   Update bucket name
-   Update access keys
-   Restart application
-   Test upload & download

------------------------------------------------------------------------

# PHASE 8 --- POST MIGRATION SAFETY

## Step 15 --- Keep Source as Backup

Do NOT delete source bucket immediately.

Recommended retention: 15--30 days after confirmation.

------------------------------------------------------------------------

# Production Best Practices

-   Enable versioning on destination bucket
-   Enable lifecycle policies
-   Enable encryption
-   Validate application functionality
-   Monitor logs after migration

------------------------------------------------------------------------

# END OF DOCUMENT
