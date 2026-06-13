import pytest
import numpy as np
from app.ml.logistic_regression import LogisticRegressionModel


def test_lr_model_initialization():
    """Test LR model initialization."""
    model = LogisticRegressionModel()
    assert model.is_trained is False


def test_lr_model_training():
    """Test LR model training."""
    model = LogisticRegressionModel()
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = np.array([0, 1, 0])
    
    metrics = model.train(X, y)
    assert model.is_trained is True
    assert 'auc' in metrics
    assert 'precision' in metrics


def test_lr_model_prediction():
    """Test LR model prediction."""
    model = LogisticRegressionModel()
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = np.array([0, 1, 0])
    
    model.train(X, y)
    predictions = model.predict(X)
    assert len(predictions) == len(X)
