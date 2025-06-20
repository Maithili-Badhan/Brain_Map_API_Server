# app/routes/regions.py

from flask import Blueprint, jsonify
from app.models import BrainRegion

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