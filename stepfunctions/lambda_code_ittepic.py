
def handler(event, context):
    print("EVENT: ",event)
    response = {
        "statusCode": 200,
        "body": "Lambda Ittepic"
    }

    return response