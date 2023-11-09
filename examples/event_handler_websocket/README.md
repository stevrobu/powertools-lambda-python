# Example for Event Handler for WebSockets

**Instructions**

1. Upload the powertools-for-lambda-python-poc.zip to an S3 bucket in your account. This zip includes the powertools changes for the WebSocket Event Handler. The SAM template will use this to create a Lambda Layer for the test Lambda.
2. From root of cloned folder: cd ./examples/event_handler_websocket
3. sam build
4. sam deploy --parameter-overrides LayerBucketName=
5. Copy the WebSocketURI output from the SAM deploy
6. In CloudShell run wscat to connect: wscat -c
7. Send the following to the connection: {action: 'joinroom'}
8. Close the connection
