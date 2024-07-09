import json
import boto3
 

eventbridge = boto3.client('events')
def handler(event, context):
    print("EVENT: ",event)
    # Configura los detalles del evento que deseas enviar a EventBridge
    event_details = {
        "detail": "Esto es una prueba"
        # Otros campos relevantes de acuerdo a tus necesidades
    }

    # Define el evento y lo envía a EventBridge
    response = eventbridge.put_events(
        Entries=[
            {
                "Source": "ULA",
                "DetailType": "EnvioDeCalificaciones",
                "Detail": json.dumps(event_details),
                "EventBusName": "eventBusTest"
            }
        ]
    )
    print("Response: ", response)

    # Respuesta HTTP exitosa
    response = {
        "statusCode": 200,
        "body": "Evento enviado a EventBridge"
    }

    return response