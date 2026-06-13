import joblib
import os
from flask import current_app
import redis
import json


class ModelStore:
    """joblib serialisation + Redis model cache."""
    
    @staticmethod
    def get_model_path(model_name, user_id=None):
        """Get file path for model."""
        if user_id:
            return os.path.join(
                current_app.config.get('MODELS_STORE_PATH', 'models_store/users'),
                f'user_{user_id}_{model_name}.joblib'
            )
        return os.path.join(
            current_app.config.get('MODELS_STORE_PATH', 'models_store'),
            f'global_{model_name}.joblib'
        )
    
    @staticmethod
    def save_model(model, model_name, user_id=None):
        """Save model to disk."""
        filepath = ModelStore.get_model_path(model_name, user_id)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(model, filepath)
    
    @staticmethod
    def load_model(model_name, user_id=None):
        """Load model from disk."""
        filepath = ModelStore.get_model_path(model_name, user_id)
        if os.path.exists(filepath):
            return joblib.load(filepath)
        return None
    
    @staticmethod
    def cache_model_metadata(model_name, metadata, user_id=None):
        """Cache model metadata in Redis."""
        cache_key = f"model:{model_name}"
        if user_id:
            cache_key = f"model:user_{user_id}:{model_name}"
        
        redis_client = redis.from_url(current_app.config['REDIS_URL'])
        redis_client.setex(
            cache_key,
            3600,  # 1 hour cache
            json.dumps(metadata)
        )
    
    @staticmethod
    def get_model_metadata(model_name, user_id=None):
        """Get model metadata from Redis."""
        cache_key = f"model:{model_name}"
        if user_id:
            cache_key = f"model:user_{user_id}:{model_name}"
        
        redis_client = redis.from_url(current_app.config['REDIS_URL'])
        data = redis_client.get(cache_key)
        
        if data:
            return json.loads(data)
        return None
