import pytest
from app.ml.feature_pipeline import FeaturePipeline
from app.ml.logistic_regression import LogisticRegressionModel


def test_recommendation_pipeline():
    """Test end-to-end recommendation pipeline."""
    # Build feature vector
    features = FeaturePipeline.build_user_feature_vector(1, 'test_token')
    assert len(features) == 8
    
    # Normalize features
    normalized = FeaturePipeline.normalize_features(features)
    assert len(normalized) == 8
    
    # Train model (placeholder)
    model = LogisticRegressionModel()
    assert model.is_trained is False
