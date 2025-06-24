import pytest
from app import create_app, db
from app.models import BrainRegion

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_post_region(client):
    payload = {
        "name": "Thalamus",
        "description": "Relay center for sensory information",
        "function": "Processes and transmits sensory data"
    }

    response = client.post("/regions/", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Thalamus"
    assert data["function"] == "Processes and transmits sensory data"