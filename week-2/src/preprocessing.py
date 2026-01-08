"""Data Preprocessing Pipeline for Week 2 Project

This module provides a reusable preprocessing pipeline for cleaning
and transforming raw datasets into model-ready formats.
"""

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from typing import Tuple


class DataPreprocessor:
    """Reusable data preprocessing pipeline."""

    def __init__(self, test_size: float = 0.2, random_state: int = 42):
        """Initialize the preprocessor.
        
        Args:
            test_size: Fraction of data to use for testing
            random_state: Random seed for reproducibility
        """
        self.test_size = test_size
        self.random_state = random_state
        self.pipeline = None
        self.numerical_features = []
        self.categorical_features = []

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        """Build and fit the preprocessing pipeline.
        
        Args:
            X: Feature matrix
            y: Target variable (optional)
        """
        # TODO: Implement pipeline fitting
        pass

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply preprocessing to data.
        
        Args:
            X: Raw feature matrix
            
        Returns:
            Preprocessed feature matrix
        """
        # TODO: Implement transformation
        pass

    def fit_transform(self, X: pd.DataFrame, y: pd.Series = None) -> pd.DataFrame:
        """Fit and transform in one step."""
        self.fit(X, y)
        return self.transform(X)

    def split_data(self, X: pd.DataFrame, y: pd.Series) -> Tuple:
        """Split data into train and test sets.
        
        Args:
            X: Feature matrix
            y: Target variable
            
        Returns:
            Tuple of (X_train, X_test, y_train, y_test)
        """
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state
        )


# Example usage
if __name__ == "__main__":
    print("Data Preprocessing Pipeline - Week 2")
    # TODO: Add example usage
