# Readme

This is a readme file for a Lambda function that copies files from an SFTP server to an S3 bucket.

## Function Purpose

The purpose of this function is to automatically copy files from an SFTP server to an S3 bucket. This can be useful for backing up files or for transferring files between servers.

## Function Arguments

The function takes two arguments:

*  `event` : The event object passed to the Lambda function.
*  `context` : The context object passed to the Lambda function.

## Function Flow

The function first gets the SFTP password from AWS Systems Manager Parameter Store.

It then creates a connection to the SFTP server and a connection to the S3 bucket.

It then copies all files from the SFTP folder to the S3 bucket.

Finally, it deletes the files from the SFTP folder.

## Function Usage

To use this function, you can create a Lambda function and upload the code to AWS Lambda. You can then configure the function to be triggered by an S3 event.