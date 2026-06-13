import pytest
import numpy as np
from app.ml.feature_pipeline import FeaturePipeline


def test_build_user_feature_vector():
    """Test feature vector construction."""
    features = FeaturePipeline.build_user_feature_vector(1, 'test_token')
    assert isinstance(features, list)
    assert len(features) == 8  # 8 audio features


def test_normalize_features():
    """Test feature normalization."""
    features = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    normalized = FeaturePipeline.normalize_features(features)
    assert isinstance(normalized, list)
    assert len(normalized) == len(features)
