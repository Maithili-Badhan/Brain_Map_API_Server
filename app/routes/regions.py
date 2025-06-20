# app/routes/regions.py

from flask import Blueprint, jsonify
from app.models import BrainRegion
from flask import request
from app import db

regions_bp = Blueprint("regions", __name__)

@regions_bp.route('/', methods=['GET'])
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

@regions_bp.route('/<int:region_id>', methods=['GET'])  # ✅ FIXED
def get_region(region_id):
    region = BrainRegion.query.get(region_id)
    if region:
        return jsonify({
            "id": region.id,
            "name": region.name,
            "description": region.description,
            "function": region.function
        }), 200
    else:
        return jsonify({"error": "Region not found"}), 404

@regions_bp.route('/', methods=['POST'])
def create_region():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "description", "function")):
        return jsonify({"error": "Missing required fields"}), 400

    new_region = BrainRegion(
        name=data["name"],
        description=data["description"],
        function=data["function"]
    )
    db.session.add(new_region)
    db.session.commit()

    return jsonify({
        "id": new_region.id,
        "name": new_region.name,
        "description": new_region.description,
        "function": new_region.function
    }), 201