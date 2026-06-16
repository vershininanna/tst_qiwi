import allure

@allure.feature("Service Health")
@allure.story("API availability")
def test_service_available(client):

    response = client.get(
        "/payment-history/v2/persons/me/payments"
    )

    assert response.status < 500

    # защита от HTML
    assert "application/json" in response.headers.get("content-type", "")

    body = response.json()
    assert body is not None