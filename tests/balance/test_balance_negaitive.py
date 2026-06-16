import allure

@allure.feature("Balance Negative")
def test_balance_not_zero(client):
    response = client.get(
        "/funding-sources/v2/persons/personId/accounts"
    )

    body = response.json()

    amount = body["accounts"][0]["balance"]["amount"]

    assert amount != 0

@allure.feature("Balance Negative")
def test_balance_not_negative(client):
    response = client.get(
        "/funding-sources/v2/persons/personId/accounts"
    )

    body = response.json()

    amount = body["accounts"][0]["balance"]["amount"]

    assert amount >= 0


@allure.feature("Balance Negative")
def test_balance_without_token(playwright):
    request = playwright.request.new_context()

    response = request.get(
        "https://edge.qiwi.com/funding-sources/v2/persons/personId/accounts"
    )

    assert response.status in (401, 403)