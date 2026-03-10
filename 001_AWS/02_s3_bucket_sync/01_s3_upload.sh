#!/bin/bash

# AWS credentials


# Directories
# SCHEDULER_DIR="/app/incred/mcollect/c2c/AudioFiles/"
# INPROGRESS_DIR="/app/incred/mcollect/c2c/InProgress/"
# COMPLETED_DIR="/app/incred/mcollect/c2c/Completed/"
# FAILED_DIR="/app/incred/mcollect/c2c/Failed/"

# S3 bucket
# S3_BUCKET="s3://mobicule-incred-files/call-recordings/prod/"


# #AWS Credentials for testing


# Export credentials for AWS CLI
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION



SCHEDULER_DIR="/home/karishma/incred_sync/AudioFiles/"               # Testing
INPROGRESS_DIR="/home/karishma/incred_sync/InProgress/"               # Testing
COMPLETED_DIR="/home/karishma/incred_sync/Completed/"                  # Testing
FAILED_DIR="/home/karishma/incred_sync/Failed/"                        # Testing


S3_BUCKET="s3://test-s3-syncing-bucket/call-recordings/prod/"               # Testing


# Log file
LOG_FILE="/home/karishma/incred_sync/s3_upload.log"

# Ensure all directories exist
mkdir -p "$INPROGRESS_DIR" "$COMPLETED_DIR" "$FAILED_DIR"

##############################
# Step 1: Retry previously failed files
##############################
for file in "$FAILED_DIR/"*; do
    [ -f "$file" ] || continue

    RETRIES=3
    COUNT=0
    SUCCESS=0

    while [ $COUNT -lt $RETRIES ]; do
        aws s3 cp "$file" "$S3_BUCKET"
        if [ $? -eq 0 ]; then
            SUCCESS=1
            break
        else
            COUNT=$((COUNT+1))
            echo "$(date): Retry $COUNT failed for previously failed file $(basename $file)" >> $LOG_FILE
            sleep 10
        fi
    done

    if [ $SUCCESS -eq 1 ]; then
        mv "$file" "$COMPLETED_DIR"
        echo "$(date): Uploaded previously failed file $(basename $file) to S3" >> $LOG_FILE
    else
        echo "$(date): Previously failed file $(basename $file) still failed after $RETRIES attempts" >> $LOG_FILE
        # File remains in FAILED_DIR for next cron retry
    fi
done

##############################
# Step 2: Move files older than 2 minutes safely (handles spaces in filenames)
find "$SCHEDULER_DIR" -type f -mmin +2 -print0 | while IFS= read -r -d '' file
do
    mv "$file" "$INPROGRESS_DIR"
done    

##############################
# Step 3: Process new files in InProgress
##############################
for file in "$INPROGRESS_DIR/"*; do
    [ -f "$file" ] || continue

    RETRIES=3
    COUNT=0
    SUCCESS=0

    while [ $COUNT -lt $RETRIES ]; do
        # aws s3 cp "$file" "$S3_BUCKET"
        aws s3 ls "$S3_BUCKET$(basename "$file")" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "$(date): File $(basename "$file") already exists in S3, skipping upload" >> $LOG_FILE
            SUCCESS=1
            break
        fi

        aws s3 cp "$file" "$S3_BUCKET"

        if [ $? -eq 0 ]; then
            SUCCESS=1
            break
        else
            COUNT=$((COUNT+1))
            echo "$(date): Retry $COUNT failed for $(basename $file)" >> $LOG_FILE
            sleep 10
        fi
    done

    if [ $SUCCESS -eq 1 ]; then
        mv "$file" "$COMPLETED_DIR"
        echo "$(date): Uploaded and moved $(basename $file)" >> $LOG_FILE
    else
        mv "$file" "$FAILED_DIR"
        echo "$(date): Failed to upload $(basename $file) after $RETRIES attempts" >> $LOG_FILE
    fi
done