import allure

@allure.feature("Balance")
@allure.story("Balance must be positive")
def test_balance_more_than_zero(client):

    response = client.get(
        "/funding-sources/v2/persons/personId/accounts"
    )

    assert response.status == 200

    body = response.json()

    assert isinstance(body, dict)

    assert "accounts" in body
    assert isinstance(body["accounts"], list)

    assert len(body["accounts"]) > 0

    account = body["accounts"][0]

    assert "alias" in account
    assert "balance" in account

    balance = account["balance"]

    assert "amount" in balance
    assert "currency" in balance

    amount = balance["amount"]

    assert isinstance(amount, (int, float))
    assert amount > 0