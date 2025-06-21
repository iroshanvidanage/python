import json, logging, boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel("INFO")


# Sample json object to publish
sample_task_details = {
    "{task_id}": {
        "platform": "{cloud_platform}",
        "service": "{cloud_service}"
    },
    "{task_id}": {
        "platform": "{cloud_platform}",
        "service": "{cloud_service}"
    },
    "{task_id}": {
        "platform": "{cloud_platform}",
        "service": "{cloud_service}"
    }
}

class SnsWrapper:
    def __init__(self, sns_topic) -> None:
        self.sns_topic = sns_topic
    

    def publish_message(self, topic_arn, task_details): 
        try:
            response =  self.sns_topic.publish(
                TopicArn=topic_arn, Message=json.dumps(task_details)
            )
            message_id = response["MessageID"]
            logger.info(f"Message published. Message ID: {message_id} to {topic_arn}")
        except ClientError:
            logger.exception(f"Couldn't publish message to {topic_arn}")
            raise
        else:
            return message_id
        

def main() -> None:

    # Initialize the SMS client
    sns_topic = boto3.client('sns')
    
    # Topic ARN
    topic_arn = 'arn:aws:sns:us-east-1:123456789012:example-topic'

    sns_publisher: SnsWrapper = SnsWrapper(sns_topic=sns_topic)
    response = sns_publisher.publish_message(topic_arn=topic_arn, task_details=sample_task_details)
    print(f"Message published, Message ID: {response}")


if __name__ == '__main__':
    main()
