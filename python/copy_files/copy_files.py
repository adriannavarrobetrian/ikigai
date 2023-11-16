import math
import os
import boto3
from boto.s3.connection import S3Connection
import io
import paramiko
import time


def lambda_handler(event, context):

    ssm = boto3.client('ssm', region_name="eu-west-1", verify=True)

    sftp_password = ssm.get_parameter(
        Name='/ERP/edi-JandJ-sftp-Password-' + os.environ['ENV'], WithDecryption=True)

    s3_conn = S3Connection()
    bucket = s3_conn.get_bucket(os.environ['S3_BUCKET_NAME'])


    transport = paramiko.Transport(
        (os.environ['SFTP_SERVER'], 22))
    transport.connect(
        username=os.environ['SFTP_USERNAME'], password=sftp_password['Parameter']['Value'])
    ftp_conn = paramiko.SFTPClient.from_transport(transport)
    print("SFTP Hostname: " + os.environ['SFTP_SERVER'])
    print("SFTP Username: " + os.environ['SFTP_USERNAME'])
    print("SFTP Folder: " + os.environ['SFTP_FOLDER'])
    print("Bucket: " + os.environ['S3_BUCKET_NAME'])
    copy_dir(os.environ['SFTP_FOLDER'], bucket, ftp_conn)
    delete_files(os.environ['SFTP_FOLDER'], ftp_conn)


def copy_file(filepath, bucket, ftp_conn):
    chunk_size = 12428800
    key_id = "/jandj/Incoming/" + \
        filepath.replace(os.environ['SFTP_FOLDER'], '').lstrip('/')
    key = bucket.get_key(key_id)
    ftp_fi = ftp_conn.file(filepath, 'r')
    source_size = ftp_fi._get_size()
    if key is not None:
        # check if we need to replace, check sizes
        if source_size == key.size:
            print('%s already uploaded' % key_id)
            ftp_fi.close()
            return

    chunk_count = int(math.ceil(source_size / float(chunk_size)))
    mp = bucket.initiate_multipart_upload(key_id)

    print('%s uploading size: %imb, %i chunks' % (
        key_id, math.ceil(source_size/1024/1024), chunk_count))
    for i in range(chunk_count):
        start = time.time()
        chunk = ftp_fi.read(chunk_size)
        end = time.time()
        seconds = end - start
        print('%s read chunk from ftp (%i/%i) %ikbs' % (
            key_id, i + 1, chunk_count,
            math.ceil((chunk_size / 1024) / seconds)))

        fp = io.BytesIO(chunk)
        start = time.time()
        mp.upload_part_from_file(fp, part_num=i + 1)
        end = time.time()
        seconds = end - start
        print('%s upload chunk to s3 (%i/%i) %ikbs' % (
            key_id, i + 1, chunk_count,
            math.ceil((chunk_size / 1024) / seconds)))

    mp.complete_upload()
    ftp_fi.close()


def copy_dir(directory, bucket, ftp_conn):
    ftp_conn.chdir(directory)
    for filename in ftp_conn.listdir():
        filepath = os.path.join(directory, filename)
        copy_file(filepath, bucket, ftp_conn)


def delete_files(directory, ftp_conn):
    ftp_conn.chdir(directory)
    for filename in ftp_conn.listdir():
        ftp_conn.remove(filename)


if __name__ == "__main__":
    lambda_handler("", "")
