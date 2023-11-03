from typing import Dict, List, Optional
from aws_lambda_powertools.utilities.data_classes.common import DictWrapper

from aws_lambda_powertools.shared.headers_serializer import (
    BaseHeadersSerializer,
    MultiValueHeadersSerializer,
)

class WebsocketEvent(DictWrapper):
    @property
    def headers(self) -> Dict[str, str]:
        return self.get("headers") or {}

    @property
    def headers(self) -> Dict[str, List[str]]:
        return self.get("multiValueHeaders") or {}

    @property
    def query_string_parameters(self) -> Optional[Dict[str, str]]:
        return self.get("queryStringParameters")

    @property
    def multi_value_query_string_parameters(self) -> Optional[Dict[str, List[str]]]:
        return self.get("multiValueQueryStringParameters")

    @property
    def request_context(self) -> Dict:
        return self.get("requestContext")

    @property
    def is_base64_encoded(self) -> Optional[bool]:
        return self.get("isBase64Encoded")

    @property
    def route_key(self) -> str:
        return self["requestContext"]["routeKey"]
    
    @property
    def event_type(self) -> str:
        return self["requestContext"]["eventType"]
    
    @property
    def connection_id(self) -> str:
        return self["requestContext"]["connectionId"]
    
    @property
    def body(self) -> str:
        return self.get("body")
    
    def header_serializer(self) -> BaseHeadersSerializer:
        return MultiValueHeadersSerializer()