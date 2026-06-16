import pytest
from api.client import ApiClient
from api.payments_api import (PaymentApi)


@pytest.fixture
def client(playwright):
    request = playwright.request.new_context()
    yield ApiClient(request)
    request.dispose()

def paments(client):
    return PaymentApi(client)
