# app/routes/regions.py

from flask import Blueprint, jsonify
from app.models import BrainRegion

regions_bp = Blueprint("regions", __name__)

@regions_bp.route("/", methods=["GET"])
def get_all_regions():
    regions = BrainRegion.query.all()
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "description": r.description,
            "function": r.function
        } for r in regions
    ])