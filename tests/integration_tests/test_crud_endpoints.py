# tests/integration_tests/test_crud_endpoints.py

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

def test_post_and_get_region(client):
    # POST
    response = client.post("/regions/", json={
        "name": "Amygdala",
        "description": "Emotion center",
        "function": "Regulates emotions"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Amygdala"

    # GET
    region_id = data["id"]
    get_response = client.get(f"/regions/{region_id}")
    assert get_response.status_code == 200
    assert get_response.get_json()["name"] == "Amygdala"

def test_update_region(client):
    # First insert a region
    client.post("/regions/", json={
        "name": "Thalamus",
        "description": "Relay",
        "function": "Relay signals"
    })

    # Update it
    response = client.put("/regions/1", json={
        "name": "Updated Thalamus",
        "function": "Sensory relay"
    })
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated Thalamus"

def test_delete_region(client):
    # First insert a region
    client.post("/regions/", json={
        "name": "DeleteMe",
        "description": "To be deleted",
        "function": "Testing"
    })

    # Delete it
    response = client.delete("/regions/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Region deleted"