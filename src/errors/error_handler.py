from src.views.http_types.http_response import HttpResponse

def handler_errors(error: Exception) -> HttpResponse:
    return HttpResponse (
        status_code=500,
        body={
            "errors":[{
                "title": "server error",
                "detail": str(error)
            }]
        }
    )
