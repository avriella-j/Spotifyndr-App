from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
import redis

db = SQLAlchemy()
socketio = SocketIO()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
login_manager = LoginManager()


def init_redis(app):
    """Initialize Redis connection."""
    return redis.from_url(app.config['REDIS_URL'])
