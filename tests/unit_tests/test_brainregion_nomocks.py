import pytest
from app import create_app, db
from app.models import BrainRegion

@pytest.fixture
def test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.drop_all()       # Force reset in case anything lingers
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()

def test_add_brainregion(test_app):
    with test_app.app_context():
        region = BrainRegion(name="Cerebellum", description="Coordinates movement", function="Motor Control")
        db.session.add(region)
        db.session.commit()

        fetched = BrainRegion.query.first()
        assert fetched.name == "Cerebellum"
        assert fetched.function == "Motor Control"

def test_repr_method(test_app):
    with test_app.app_context():
        region = BrainRegion(name="Amygdala", description="Emotion", function="Fear response")
        db.session.add(region)
        db.session.commit()

        assert str(region) == "<BrainRegion Amygdala>"