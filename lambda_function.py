import json

def lambda_handler(event, context):
    # TODO implement
    print('from pipeline')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
