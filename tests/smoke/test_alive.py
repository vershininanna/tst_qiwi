import allure


@allure.feature("Service Health")
@allure.story("API availability")
def test_service_available(client):

    response = client.get(
        "/person-profile/v1/profile/current"
    )

    assert response.status in (200, 401, 403)

    assert "application/json" in response.headers.get(
        "content-type", ""
    )

    body = response.json()

    assert body is not None
    assert isinstance(body, dict)

    if response.status == 200:
        assert "authInfo" in body
        assert "contractInfo" in body