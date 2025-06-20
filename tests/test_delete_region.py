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

def test_delete_region(client):
    # Insert a region to delete
    with client.application.app_context():
        region = BrainRegion(name="To Delete", description="Some desc", function="Some func")
        db.session.add(region)
        db.session.commit()
        region_id = region.id

    response = client.delete(f"/regions/{region_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Region deleted"