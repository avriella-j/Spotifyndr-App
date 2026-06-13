from flask import jsonify, request
from flask_login import login_required, current_user
from app.services.user_service import UserService


@login_required
def get_users():
    """Get list of users with pagination."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    users = UserService.get_users_paginated(page, per_page)
    return jsonify([user.to_dict() for user in users.items])


@login_required
def get_user(user_id):
    """Get user by ID."""
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())


@login_required
def update_user(user_id):
    """Update user profile."""
    if user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    user = UserService.update_user(user_id, data)
    return jsonify(user.to_dict())


@login_required
def delete_user(user_id):
    """Delete user account."""
    if user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    UserService.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'})
