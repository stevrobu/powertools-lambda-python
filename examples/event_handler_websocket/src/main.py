import random
import string
import boto3
import os

from aws_lambda_powertools.event_handler.api_gateway import WebsocketRouter, WebsocketResolver

app = WebsocketResolver(debug=True)
router = WebsocketRouter()
# Get main_server_api_url from environment variables
main_server_api_url_prefix = os.environ['MainServerAPIUrlPrefix']
region = os.environ['AWS_REGION']
main_server_api_url = f"https://{main_server_api_url_prefix}.execute-api.{region}.amazonaws.com/Dev"

# Handle on connect
@router.route('$connect')
def connect():
    # if connectionId is not included in the query string, generate a random one
    tmp_guest_user_id = ''.join(random.choices(string.ascii_uppercase+string.digits, k=12))
    user_id = router.current_event.get("queryStringParameters", {"user_id": tmp_guest_user_id}).get('user_id')
    connection_id = router.current_event.connection_id
    print(f"connect user_id: {user_id}, connection_id: {connection_id}") # print user_id and connection_id, so we can find that in CloudWatch Log
    return {}, 200

# Handle on disconnect
@router.route('$disconnect')
def disconnect():
    connection_id = router.current_event.connection_id
    print(f"disconnect connection_id: {connection_id}") 
    return {}, 200

# Send data to client by APIGatewayManagementAPI
# WSS_SERVER is the domain of APIGateway
def server_response(connection_id, message):
    try:
        print(main_server_api_url)
        apig_management_client = boto3.client('apigatewaymanagementapi',endpoint_url=main_server_api_url)
        send_response = apig_management_client.post_to_connection(Data=message, ConnectionId=connection_id)
    except Exception as e:
        print(e)

@router.route('joinroom')
def join_room():
    connection_id = router.current_event.connection_id

    # response json data to client after joining room
    message = 'ConnectionId: %s joined the room.'% connection_id
    server_response(connection_id, message)

    return 200

app.include_router(router)

def main_handler(event, context):
    try:
        return app.resolve(event, context)
    except Exception as err:
        print(err)
        
        return 500

