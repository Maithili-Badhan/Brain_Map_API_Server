# app/models.py

from app import db

class BrainRegion(db.Model):
    __tablename__ = 'brain_regions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    function = db.Column(db.String(255))