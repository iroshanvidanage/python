import json, os, logging

logger = logging.getLogger()
logger.setLevel("INFO")



def get_task_data():
    """
    Helper function to fetch the open tasks
    Returns:
        Dict containing the information and parameters related to each specific task
    """

    ...


def assign_engineer(task_data):
    """
    Helper function to determine the engineer to be assigned to a task
    Parameters:
        task_data: Dict containing the information and parameters related to each specific task
    """
    """
    Finally notify the engineer
    """

    engineer = {
        "name": "Lorem Ipsum",
        "email": "lorem.ipsum@example.com",
        "mobile": "+++++++++++++++++++++++"
    }

    task = task_data['task_id']

    notify_engineer(engineer=engineer, task=task)


def notify_engineer(engineer, task):
    """
    Helper function to notify each engineer, the task they are assigned to
    Parameters:
        engineer: Dict containing the engineer's contact information
        task: Dict containing the task details
    """
    ...


def lambda_handler(event, context):
    """
    Main Lambda handler function
    """
    trigger_source = context.invoked_function_arn.split(':')[2]

    # Check for SNS trigger
    if "Records" in event and event["Records"][0].get("EventSource") == "aws:sns":
        trigger_source = "sns"
        message_details = json.loads(event["Records"][0]["Sns"]["Message"])
    
    # Check for EventBridge trigger
    elif "source" in event and "detail-type" in event:
        trigger_source = "event"
    else:
        logger.error(f"Unknown trigger source {event}")
        return {
            "statusCode": 400,
            "body": "Unsupported trigger source"
        }

    source = {
        "event": {
            "print": "Triggered by EventRule"
        },
        "sns": {
            "print": "Triggered by SNS"
        }
    }
    logger.info(source[trigger_source]["print"])
    
    # The lambda invoked by SNS will contains the task related data
    example_event = {
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

    if trigger_source == "sns":
        logger.info(f"Task assignment triggered by SNS is executing for {','.join(event.keys())}")
        assign_engineer(task_data=message_details)
        return
    
    # If not triggered by the SNS should proceed with the regular operation
    tasks_in_queue = get_task_data()
    assign_engineer(task_data=tasks_in_queue)
    
