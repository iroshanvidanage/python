import json, os, logging, boto3

logger = logging.getLogger()
logger.setLevel("INFO")

s3_client = boto3.client('s3')

def upload_receipt_to_s3(bucket_name, key, receipt_content):
    """Helper function to upload receipt to S3"""
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=receipt_content
        )
    except Exception as e:
        logger.error(f"Failed to upload receipt to S3: {str(e)}")
        raise

def lambda_handler(event, context):
    """
    Main Lambda handler function
    Parameters:
        event: Dict containing the Lambda function event data
        context: Lambda runtime context
    Returns:
        Dict containing status message
    """
    try:
        order_id = event['Order_id']
        amount = event['Amount']
        item = event['Item']

        bucket_name = os.environ.get('RECEIPT_BUCKET')
        if not bucket_name:
            raise ValueError("Missing required environment variable RECEIPT_BUCKET")
        
        logger.debug(f"Creating the receipt content for OrderID {order_id}")
        receipt_content = (
            f"OrderID: {order_id}\n"
            f"Amount: ${amount}\n"
            f"Item: {item}"
        )
        logger.debug(f"Order receipt content created for OrderID {order_id}")

        key = f"receipts/{order_id}.txt"

        upload_receipt_to_s3(bucket_name=bucket_name, key=key, receipt_content=receipt_content)

        logger.info(f"Successfully processed order {order_id} and stored receipt in S3 bucket {bucket_name}")

        return {
            "statusCode": 200,
            "message": "Receipt processed successfully"
        }
    
    except Exception as e:
        logger.error(f"Error processing order: {str(e)}")
        raise