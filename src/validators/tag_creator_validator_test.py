from src.errors.erros_type.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def teste_tag_creator_validator():
    req = MockRequest(json={"product_code": "12345"})
    tag_creator_validator(req)

def teste_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code": 12345})

    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
