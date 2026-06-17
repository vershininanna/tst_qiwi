from config.settings import BASE_URL, TOKEN

class ApiClient:
    def __init__(self, request):
        self.request = request
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        }

    def get(self, endpoint):
        response = self.request.get(
            f"{BASE_URL}{endpoint}",
            headers=self.headers,
        )
        return response

    def post(self, endpoint, body):
        response = self.request.post(
            f"{BASE_URL}{endpoint}",
            headers=self.headers,
            data=body,
        )
        return response