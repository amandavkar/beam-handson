from google.cloud import pubsub_v1
import time
import os

if __name__ == "__main__":
    
    # Replace 'my-service-account-path' with your service account path
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'curious-ivy-273110-7fbea74bc1b3.json'
    
    # Replace 'my-subscription' with your subscription id
    subscription_path = 'projects/curious-ivy-273110/subscriptions/Subscribe2'
    
    subscriber = pubsub_v1.SubscriberClient()
 
    def callback(message):
        print(('Received message: {}'.format(message)))    
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    while True:
        time.sleep(60)