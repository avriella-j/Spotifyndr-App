from app.models.recommendation_event import RecommendationEvent
from app.models.swipe import Swipe
from app.extensions import db
import random


class RecommendationService:
    """Recommendation logic."""
    
    @staticmethod
    def get_user_recommendations(user_id, limit=10):
        """Get personalized recommendations for FYP."""
        # In a real implementation, this would use ML models
        # For now, return random content
        from app.models.user_feature_vector import UserFeatureVector
        
        feature_vector = UserFeatureVector.query.filter_by(user_id=user_id).first()
        
        # Placeholder: return empty list
        return []
    
    @staticmethod
    def submit_feedback(user_id, rec_id, liked):
        """Submit feedback on a recommendation."""
        rec = RecommendationEvent.query.get(rec_id)
        if not rec:
            return
        
        rec.feedback = liked
        db.session.commit()
    
    @staticmethod
    def get_explore_content(user_id, limit=10):
        """Get explore content for swipe interface."""
        # Placeholder: return empty list
        return []
    
    @staticmethod
    def record_swipe(user_id, content_id, liked):
        """Record swipe action."""
        swipe = Swipe(
            user_id=user_id,
            content_id=content_id,
            content_type='track',  # Default to track
            liked=liked
        )
        db.session.add(swipe)
        db.session.commit()
