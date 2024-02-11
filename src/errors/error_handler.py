from src.views.http_types.http_response import HttpResponse
from .erros_type.http_unprocessable_entity import HttpUnprocessableEntityError

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse (
        status_code=500,
        body={
            "errors":[{
                "title": "server error",
                "detail": str(error)
            }]
        }
    )
