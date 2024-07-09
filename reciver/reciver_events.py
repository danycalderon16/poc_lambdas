import json
import boto3

# Recupera el ARN de SSM Parameter Store
ssm = boto3.client('ssm')
parameter_name = '/myapp/first_stepfunction_arn'
response = ssm.get_parameter(Name=parameter_name)
step_function_arn = response['Parameter']['Value']


stepFunction = boto3.client('stepfunctions')
 

def handler(event, context):
    print("event", event['Records'][0]['body'])
    # Parsea el JSON contenido en el campo 'body'
    body_data = json.loads(event['Records'][0]['body'])


    # Accede a los valores de 'source' y 'eventType'
    source = body_data.get('source')
    eventType = body_data.get('detail-type')
    detail = body_data.get('detail')
    # Tu objeto JSON como diccionario Python
    input_data = {"source": source, "eventType": eventType, "detail" : detail}

    # Convierte el objeto JSON en una cadena (string) JSON
    input_string = json.dumps(input_data)
    response = stepFunction.start_execution(
        stateMachineArn=step_function_arn,
        # input=input_string
    )

    # TODO implement
    return {
        'statusCode': 200, 
        'body': json.dumps('Hello from Lambda reciver!')
    }