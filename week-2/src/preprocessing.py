"""Data Preprocessing Pipeline for Week 2 Project

This module provides a reusable preprocessing pipeline for cleaning
and transforming raw datasets into model-ready formats.
"""
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, SimpleImputer
from sklearn.model_selection import train_test_split
from typing import Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


class DataPreprocessor:
    """Reusable data preprocessing pipeline with modular components.
    
    Features:
    - Missing value imputation (mean/median/mode)
    - Categorical encoding (OneHot)
    - Numerical scaling (StandardScaler)
    - Train-test splitting
    - Sklearn-compatible pipeline design
    """
    
    def __init__(
        self,
        test_size: float = 0.2,
        random_state: int = 42,
        imputation_strategy: str = 'mean',
        scaling_strategy: str = 'standard'
    ):
        """Initialize the preprocessor.
        
        Args:
            test_size: Fraction of data to use for testing (default: 0.2)
            random_state: Random seed for reproducibility (default: 42)
            imputation_strategy: Strategy for missing values - 'mean', 'median', 'most_frequent' (default: 'mean')
            scaling_strategy: Strategy for scaling - 'standard', 'minmax' (default: 'standard')
        """
        self.test_size = test_size
        self.random_state = random_state
        self.imputation_strategy = imputation_strategy
        self.scaling_strategy = scaling_strategy
        
        self.pipeline = None
        self.numerical_features = []
        self.categorical_features = []
        self.is_fitted = False
        
    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None):
        """Build and fit the preprocessing pipeline.
        
        Args:
            X: Feature matrix (DataFrame)
            y: Target variable (optional, not used in fit but kept for sklearn compatibility)
            
        Returns:
            self: Fitted preprocessor
        """
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X must be a pandas DataFrame")
        
        # Identify feature types
        self.numerical_features = X.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # Build sklearn ColumnTransformer pipeline
        transformers = []
        
        # Numerical pipeline: Impute + Scale
        if len(self.numerical_features) > 0:
            numerical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy=self.imputation_strategy)),
                ('scaler', StandardScaler())
            ])
            transformers.append(('num', numerical_pipeline, self.numerical_features))
        
        # Categorical pipeline: Impute + OneHot Encode
        if len(self.categorical_features) > 0:
            categorical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
            ])
            transformers.append(('cat', categorical_pipeline, self.categorical_features))
        
        # Create main pipeline
        self.pipeline = ColumnTransformer(
            transformers=transformers,
            remainder='passthrough'  # Keep any remaining columns
        )
        
        # Fit the pipeline
        self.pipeline.fit(X)
        self.is_fitted = True
        
        return self
    
    def transform(self, X: pd.DataFrame) -> np.ndarray:
        """Apply preprocessing to data.
        
        Args:
            X: Raw feature matrix (DataFrame)
            
        Returns:
            Preprocessed feature matrix (numpy array)
            
        Raises:
            ValueError: If preprocessor hasn't been fitted yet
        """
        if not self.is_fitted:
            raise ValueError("Preprocessor must be fitted before transform. Call fit() first.")
        
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X must be a pandas DataFrame")
        
        return self.pipeline.transform(X)
    
    def fit_transform(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> np.ndarray:
        """Fit and transform in one step.
        
        Args:
            X: Feature matrix (DataFrame)
            y: Target variable (optional)
            
        Returns:
            Preprocessed feature matrix (numpy array)
        """
        return self.fit(X, y).transform(X)
    
    def split_data(
        self,
        X: pd.DataFrame,
        y: pd.Series
    ) -> Tuple[np.ndarray, np.ndarray, pd.Series, pd.Series]:
        """Split data into train and test sets BEFORE preprocessing.
        
        This prevents data leakage by ensuring statistics (mean, std) are learned
        only from training data.
        
        Args:
            X: Feature matrix (DataFrame)
            y: Target variable (Series)
            
        Returns:
            Tuple of (X_train_raw, X_test_raw, y_train, y_test)
        """
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X must be a pandas DataFrame")
        if not isinstance(y, pd.Series):
            raise TypeError("y must be a pandas Series")
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state
        )
        
        return X_train, X_test, y_train, y_test
    
    def get_feature_names_out(self) -> list:
        """Get names of features after preprocessing.
        
        Returns:
            List of feature names
        """
        if not self.is_fitted:
            raise ValueError("Preprocessor must be fitted first.")
        
        if hasattr(self.pipeline, 'get_feature_names_out'):
            return list(self.pipeline.get_feature_names_out())
        else:
            return [f'feature_{i}' for i in range(self.pipeline.transform(pd.DataFrame()).shape[1])]


def run_pipeline(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    imputation_strategy: str = 'mean',
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, pd.Series, pd.Series]:
    """Convenience function to run the full preprocessing pipeline.
    
    This function handles the complete workflow:
    1. Split data (to prevent data leakage)
    2. Fit preprocessor on training data
    3. Transform both train and test sets
    
    Args:
        X: Feature matrix (DataFrame)
        y: Target variable (Series)
        test_size: Fraction of data for testing (default: 0.2)
        imputation_strategy: Strategy for missing values (default: 'mean')
        random_state: Random seed (default: 42)
        
    Returns:
        Tuple of (X_train_processed, X_test_processed, y_train, y_test)
        
    Example:
        >>> import pandas as pd
        >>> from src.preprocessing import run_pipeline
        >>> df = pd.read_csv('data/raw/dataset.csv')
        >>> X = df.drop('target', axis=1)
        >>> y = df['target']
        >>> X_train, X_test, y_train, y_test = run_pipeline(X, y, test_size=0.2)
    """
    
    # Initialize preprocessor
    preprocessor = DataPreprocessor(
        test_size=test_size,
        random_state=random_state,
        imputation_strategy=imputation_strategy
    )
    
    # Split data first (critical to prevent data leakage!)
    X_train, X_test, y_train, y_test = preprocessor.split_data(X, y)
    
    # Fit on training data only
    preprocessor.fit(X_train)
    
    # Transform both sets
    X_train_processed = preprocessor.transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    return X_train_processed, X_test_processed, y_train, y_test


# Example usage
if __name__ == "__main__":
    print("Data Preprocessing Pipeline - Week 2")
    print("=====================================\n")
    print("Usage:")
    print("  from src.preprocessing import DataPreprocessor, run_pipeline")
    print("  import pandas as pd\n")
    print("  # Option 1: Using run_pipeline()")
    print("  df = pd.read_csv('data/raw/titanic.csv')")
    print("  X = df.drop('Survived', axis=1)")
    print("  y = df['Survived']")
    print("  X_train, X_test, y_train, y_test = run_pipeline(X, y)\n")
    print("  # Option 2: Using DataPreprocessor class")
    print("  preprocessor = DataPreprocessor(test_size=0.2)")
    print("  X_train, X_test, y_train, y_test = preprocessor.split_data(X, y)")
    print("  preprocessor.fit(X_train)")
    print("  X_train_processed = preprocessor.transform(X_train)")
    print("  X_test_processed = preprocessor.transform(X_test)")
