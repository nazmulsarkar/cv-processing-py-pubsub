import os
from google.cloud import pubsub_v1
import ast
import time

credentials_path = '../ph-api-dev-c7f82a89c4e0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

#PROJECT_ID = os.environ['project_id']
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    'ph-api-dev', 'contact-ids-depo-sub')

while True:
    response = subscriber.pull(
        request={
            "subscription": subscription_path,
            "max_messages": 10,
        }
    )

    # if not response.received_messages:
    #     print('❌ no messages in pub/sub')
    #     break

    for msg in response.received_messages:
        message_data = ast.literal_eval(msg.message.data.decode('utf-8'))
        # transform data and publish to another topic

        time.sleep(2.4)
        print("Pushed to another topic 2.4 seconds.")

    ack_ids = [msg.ack_id for msg in response.received_messages]
    subscriber.acknowledge(
        request={
            "subscription": subscription_path,
            "ack_ids": ack_ids,
        }
    )


print('🏁 No more messages left in the queue. Shutting down...')
