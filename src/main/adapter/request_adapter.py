from typing import Callable, Type

from flask import request as FlaskRequest
from src.views.http_types.http_request import HttpRequest

def request_adapter(request: FlaskRequest) -> HttpRequest:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=request.args,
        url=request.full_path,
    )
    return http_request

   
    