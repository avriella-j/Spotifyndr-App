from app.models.user import User
from app.extensions import db
from app.services.token_service import TokenService


class UserService:
    """User CRUD and profile logic."""
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID."""
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_spotify_id(spotify_id):
        """Get user by Spotify ID."""
        return User.query.filter_by(spotify_id=spotify_id).first()
    
    @staticmethod
    def get_users_paginated(page=1, per_page=20):
        """Get paginated list of users."""
        return User.query.paginate(page=page, per_page=per_page, error_out=False)
    
    @staticmethod
    def get_or_create_user(spotify_id, display_name, email, images, access_token, refresh_token, expires_at):
        """Get existing user or create new one."""
        user = UserService.get_user_by_spotify_id(spotify_id)
        
        if not user:
            image_url = images[0]['url'] if images else None
            user = User(
                spotify_id=spotify_id,
                display_name=display_name,
                email=email,
                image_url=image_url,
                access_token=TokenService.encrypt_token(access_token),
                refresh_token=TokenService.encrypt_token(refresh_token),
                token_expires_at=expires_at
            )
            db.session.add(user)
        else:
            user.display_name = display_name
            user.email = email
            user.access_token = TokenService.encrypt_token(access_token)
            user.refresh_token = TokenService.encrypt_token(refresh_token)
            user.token_expires_at = expires_at
        
        db.session.commit()
        return user
    
    @staticmethod
    def update_user(user_id, data):
        """Update user profile."""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None
        
        if 'display_name' in data:
            user.display_name = data['display_name']
        if 'image_url' in data:
            user.image_url = data['image_url']
        
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        """Delete user account."""
        user = UserService.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
    
    @staticmethod
    def get_user_settings(user_id):
        """Get user settings."""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None
        
        return {
            'display_name': user.display_name,
            'image_url': user.image_url,
            'email': user.email
        }
    
    @staticmethod
    def update_user_settings(user_id, data):
        """Update user settings."""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None
        
        if 'display_name' in data:
            user.display_name = data['display_name']
        if 'image_url' in data:
            user.image_url = data['image_url']
        
        db.session.commit()
        return UserService.get_user_settings(user_id)
