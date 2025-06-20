# create_db.py

from app import create_app, db
from app.models import BrainRegion

app = create_app()

with app.app_context():
    db.create_all()