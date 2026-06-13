from flask import jsonify, request
from flask_login import login_required, current_user
from app.services.recommendation_service import RecommendationService


@login_required
def get_explore_content():
    """Get explore content for swipe interface."""
    limit = request.args.get('limit', 10, type=int)
    content = RecommendationService.get_explore_content(current_user.id, limit)
    return jsonify([c.to_dict() for c in content])


@login_required
def submit_swipe():
    """Submit swipe action (like/dislike)."""
    data = request.get_json()
    content_id = data.get('content_id')
    liked = data.get('liked', False)
    
    RecommendationService.record_swipe(current_user.id, content_id, liked)
    return jsonify({'message': 'Swipe recorded successfully'})
