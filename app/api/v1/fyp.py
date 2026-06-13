from flask import jsonify, request
from flask_login import login_required, current_user
from app.services.recommendation_service import RecommendationService


@login_required
def get_recommendations():
    """Get personalized recommendations for FYP."""
    limit = request.args.get('limit', 10, type=int)
    recommendations = RecommendationService.get_user_recommendations(current_user.id, limit)
    return jsonify([r.to_dict() for r in recommendations])


@login_required
def submit_feedback(rec_id):
    """Submit feedback on a recommendation."""
    data = request.get_json()
    liked = data.get('liked', False)
    
    RecommendationService.submit_feedback(current_user.id, rec_id, liked)
    return jsonify({'message': 'Feedback submitted successfully'})
