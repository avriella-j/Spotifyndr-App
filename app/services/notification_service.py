from app.models.notification import Notification
from app.extensions import db


class NotificationService:
    """Notification logic."""
    
    @staticmethod
    def get_user_notifications(user_id):
        """Get user's notifications."""
        return Notification.query.filter_by(user_id=user_id).order_by(Notification.created_at.desc()).all()
    
    @staticmethod
    def create_notification(user_id, notification_type, title, message, data=None):
        """Create a new notification."""
        notification = Notification(
            user_id=user_id,
            type=notification_type,
            title=title,
            message=message,
            data=data
        )
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def mark_as_read(notification_id):
        """Mark notification as read."""
        notification = Notification.query.get(notification_id)
        if notification:
            notification.read = True
            db.session.commit()
    
    @staticmethod
    def mark_all_as_read(user_id):
        """Mark all notifications as read for a user."""
        Notification.query.filter_by(user_id=user_id).update({'read': True})
        db.session.commit()
