from flask import Blueprint

api_bp = Blueprint('api', __name__)

from app.api.v1 import users, follows, fyp, explore, mutuals, messaging, settings, notifications

api_bp.add_url_rule('/users', view_func=users.get_users, methods=['GET'])
api_bp.add_url_rule('/users/<int:user_id>', view_func=users.get_user, methods=['GET'])
api_bp.add_url_rule('/users/<int:user_id>', view_func=users.update_user, methods=['PUT'])
api_bp.add_url_rule('/users/<int:user_id>', view_func=users.delete_user, methods=['DELETE'])

api_bp.add_url_rule('/follows/<int:user_id>', view_func=follows.follow_user, methods=['POST'])
api_bp.add_url_rule('/follows/<int:user_id>', view_func=follows.unfollow_user, methods=['DELETE'])
api_bp.add_url_rule('/follows/<int:user_id>/followers', view_func=follows.get_followers, methods=['GET'])
api_bp.add_url_rule('/follows/<int:user_id>/following', view_func=follows.get_following, methods=['GET'])

api_bp.add_url_rule('/fyp', view_func=fyp.get_recommendations, methods=['GET'])
api_bp.add_url_rule('/fyp/<int:rec_id>/feedback', view_func=fyp.submit_feedback, methods=['POST'])

api_bp.add_url_rule('/explore', view_func=explore.get_explore_content, methods=['GET'])
api_bp.add_url_rule('/explore/swipe', view_func=explore.submit_swipe, methods=['POST'])

api_bp.add_url_rule('/mutuals', view_func=mutuals.find_mutuals, methods=['GET'])

api_bp.add_url_rule('/messaging/conversations', view_func=messaging.get_conversations, methods=['GET'])
api_bp.add_url_rule('/messaging/conversations', view_func=messaging.create_conversation, methods=['POST'])
api_bp.add_url_rule('/messaging/conversations/<int:conversation_id>/messages', view_func=messaging.get_messages, methods=['GET'])
api_bp.add_url_rule('/messaging/conversations/<int:conversation_id>/messages', view_func=messaging.send_message, methods=['POST'])

api_bp.add_url_rule('/settings', view_func=settings.get_settings, methods=['GET'])
api_bp.add_url_rule('/settings', view_func=settings.update_settings, methods=['PUT'])

api_bp.add_url_rule('/notifications', view_func=notifications.get_notifications, methods=['GET'])
api_bp.add_url_rule('/notifications/<int:notification_id>/read', view_func=notifications.mark_read, methods=['PUT'])
