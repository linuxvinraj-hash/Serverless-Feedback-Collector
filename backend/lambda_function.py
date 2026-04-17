import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('feedback-table')


# ✅ Helper to fix Decimal issue
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


def lambda_handler(event, context):
    path = event.get('rawPath')
    method = event.get('requestContext', {}).get('http', {}).get('method')

    # POST /feedback
    if path == "/feedback" and method == "POST":
        try:
            body = json.loads(event.get('body', '{}'))

            feedback_id = str(uuid.uuid4())

            table.put_item(Item={
                'id': feedback_id,
                'name': body.get('name', 'Anonymous'),
                'email': body.get('email', 'N/A'),
                'message': body.get('message', ''),
                'timestamp': datetime.utcnow().isoformat()
            })

            return response(201, {
                "message": "Feedback submitted successfully!",
                "id": feedback_id
            })

        except Exception as e:
            return response(500, {"error": str(e)})

    # GET /admin/feedback
    elif path == "/admin/feedback" and method == "GET":
        try:
            result = table.scan(Limit=10)
            items = result.get('Items', [])

            return response(200, items)

        except Exception as e:
            return response(500, {"error": str(e)})

    # Default
    return response(404, {"error": "Not Found"})


def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # CORS
        },
        "body": json.dumps(body, default=decimal_default)  # ✅ FIX APPLIED HERE
    }
