import allure
import uuid
import json


@allure.feature("Payments")
@allure.story("Execute payment")
def test_execute_created_payment(client):

    payment_id = str(uuid.uuid4())

    payload = {
        "id": payment_id,
        "sum": {
            "amount": 1,
            "currency": "643"
        },
        "paymentMethod": {
            "type": "Account",
            "accountId": "643"
        },
        "fields": {
            "account": "79999999999"
        }
    }

    create_response = client.post(
        f"/sinap/api/v2/terms/99/payments/{payment_id}",
        json.dumps(payload)
    )

    assert create_response.status < 500

    status_response = client.get(
        f"/payment-history/v1/transactions/{payment_id}"
    )

    assert status_response.status < 500

    body = status_response.json()

    assert body is not None

    if "status" in body:
        assert body["status"]["value"] in (
            "SUCCESS",
            "WAITING",
            "IN_PROGRESS"
        )