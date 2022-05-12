import requests
from google.cloud import storage, vision
from wand.image import Image
from credentials import CHAT_ID, BOT_TOKEN

client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

def check_image(data):
    file_data = data

    file_name = file_data["name"]
    bucket_name = file_data["bucket"]

    # Image path stored in bucket
    blob_uri = f"gs://{bucket_name}/{file_name}"
    print(f"Analyzing {file_name}.")

    # Call Vision API
    num_faces = detect_faces(blob_uri)

    # Send Http request to Telegram Bot API
    if num_faces > 0:
        print("telegram msg")
        object_url = f"https://storage.googleapis.com/{bucket_name}/{file_name}"
        data = {'chat_id':CHAT_ID, 'photo':object_url, 'caption':"⚠️Persona detectada"}
        requests.post(f"https://api.telegram.org/{BOT_TOKEN}/sendPhoto", data=data)

    return


def detect_faces(path):
    """Return number of faces in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    try:
        image = vision.Image(source=vision.ImageSource(image_uri=path))

        response = client.face_detection(image=image)
        faces = response.face_annotations

        print('Faces:')
        print(len(faces))
        return len(faces)

    except:
        return 0
