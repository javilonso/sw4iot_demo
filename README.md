# sw4iot_demo

This is a simple project that covers an IoT architecture, from hardware to Cloud.
The use case selected to replicate with this architecture is a Video Surveillance Detection Camera (like Google Nest Cam).

![alt text](https://github.com/javilonso/sw4iot_demo/blob/main/schema.png?raw=true)

1. A Raspberry Pi 3 (IoT device) takes an image every 2 seconds.
2. Each image is uploaded to a Google Cloud Bucket.
3. The Bucket publishes a message (trigger) to a Topic (Google Pub/Sub).
4. A service (Google Cloud Run Container) is subscribed to the Topic. When a new image arrives, the service processes the image and calls the Google Vision API.
5. The Google Vision API responses with a Json object that contains the human faces detected on the image.
6. In case there is any person on the image, an Http request is sent through the Telegram Bot API to get the notification.
