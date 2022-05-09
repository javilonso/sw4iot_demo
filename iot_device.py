import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/credentials.json"
from google.cloud import storage

from picamera import PiCamera
from time import time, sleep


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

camera = PiCamera()
while True:
  file_name = str(int(time())) + ".jpg"
  camera.capture(file_name)
  upload_blob("iot-demo-bucket", file_name, file_name)
  sleep(2)
