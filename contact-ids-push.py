import os
from google.cloud import pubsub_v1

credentials_path = '/Users/nhassan/bit/TilR/ph-api-dev-c7f82a89c4e0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/ph-api-dev/topics/contact-ids-depo'


for x in range(2):
    data = 'A cv is ready for processing!'
    data = data.encode('utf-8')
    attributes = {
        'cvName': "cv-00% s" % x,
        'cvEmail': 'some@yopmail.com',
        'cvPhone': '+657902345'
    }
    future = publisher.publish(topic_path, data, **attributes)
    print(f'published message id {future.result()}')
