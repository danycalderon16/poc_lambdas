import json

def handler(event, context):
    print("EVENT: ",event)
    response = {
        "statusCode": 200,
        "body": "Hola mundo"
    }

    return response