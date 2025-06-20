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

def test_update_region(client):
    # Add sample data
    with client.application.app_context():
        sample = BrainRegion(name="Test", description="Desc", function="Func")
        db.session.add(sample)
        db.session.commit()
        sample_id = sample.id  # capture the ID before context ends

    # Perform PUT request
    response = client.put(f"/regions/{sample_id}", json={
        "name": "Updated",
        "function": "Updated Function"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Updated"
    assert data["function"] == "Updated Function"