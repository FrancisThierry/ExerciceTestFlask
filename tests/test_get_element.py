import pytest
import json

from src.application import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


class TestFlaskAppElements:
    def test_get_element_by_atomic_number_success(self, client):
        response = client.get("/element/88")
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data}")
        assert response.status_code == 200

        # Décoder les octets en une chaîne de caractères, puis charger en JSON
        data = json.loads(response.data.decode('utf-8')) # Modifiez cette ligne

        print(f"Response JSON: {data.get('atomic_number')}") # Utilisez .get() pour accéder aux clés
        assert data == {
            "atomic_number": "88",
            "name": "Radium",
            "symbol": "Ra"
        }