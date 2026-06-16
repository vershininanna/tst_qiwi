import allure

@allure.feature("Balance")
@allure.story("Balance must be positive")
def test_balance_more_than_zero(client):
    response = client.get(
        "/funding-sources/v2/persons/personId/accounts"
    )

    print('STATUS:', response.status)
    print("HEADERS:", response.headers)
    print("TEXT:", response.text())

    assert response.status < 500

    body = response.json()

    assert "accounts" in body
    assert len(body["accounts"]) > 0

    amount = body["accounts"][0]["balance"]["amount"]

    assert isinstance(amount, (int, float))
    assert amount > 0