import allure

@allure.feature("User Profile")
@allure.story("Get current QIWI profile")
def test_get_user_profile(client):

    response = client.request.get(
        "https://edge.qiwi.com/person-profile/v1/profile/current",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {client.headers['Authorization'].split(' ')[1]}"
        }
    )

    print("\nSTATUS:", response.status)
    print("\nHEADERS:", response.headers)
    print("\nRAW TEXT:", response.text())

    assert response.status == 200
    assert "application/json" in response.headers.get("content-type", "")

    body = response.json()

    print("\n=== USER PROFILE ===")
    print("ID:", body.get("authInfo", {}).get("personId"))
    print("Contract ID:", body.get("contractInfo", {}).get("contractId"))
    print("Full name:", body.get("contractInfo", {}).get("name"))
    print("Status:", body.get("contractInfo", {}).get("status"))

    print("\n=== WALLET INFO ===")

    balances = body.get("balances", {})

    for currency, data in balances.items():
        print(f"\nCurrency: {currency}")
        print("Amount:", data.get("amount"))
        print("Available:", data.get("amount", 0))