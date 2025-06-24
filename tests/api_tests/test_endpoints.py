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

def test_get_all_regions(client):
    response = client.get("/regions/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_post_region(client):
    payload = {
        "name": "Amygdala",
        "description": "Emotion center",
        "function": "Process emotions"
    }
    response = client.post("/regions/", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Amygdala"

def test_get_region_by_id(client):
    # First insert
    region = BrainRegion(name="Thalamus", description="Relay center", function="Sensory gateway")
    with client.application.app_context():
        db.session.add(region)
        db.session.commit()
        region_id = region.id

    response = client.get(f"/regions/{region_id}")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Thalamus"

def test_update_region(client):
    with client.application.app_context():
        region = BrainRegion(name="Cortex", description="...", function="...")
        db.session.add(region)
        db.session.commit()
        region_id = region.id

    updated = {
        "name": "Updated Cortex",
        "function": "Advanced Thinking"
    }
    response = client.put(f"/regions/{region_id}", json=updated)
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated Cortex"

def test_delete_region(client):
    with client.application.app_context():
        region = BrainRegion(name="To Delete", description="...", function="...")
        db.session.add(region)
        db.session.commit()
        region_id = region.id

    response = client.delete(f"/regions/{region_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Region deleted"