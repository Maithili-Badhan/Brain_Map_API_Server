import pytest
from app import create_app, db
from models import BrainRegion

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()

            sample = BrainRegion(
                name="Amygdala",
                description="Processes emotions",
                function="Fear and threat detection"
            )
            db.session.add(sample)
            db.session.commit()
        yield client

def test_get_one_region(client):
    response = client.get("/regions/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Amygdala"
    assert data["function"] == "Fear and threat detection"