#!/usr/bin/env python
"""
Week 2: Quick Start Demo for Preprocessing Pipeline

This script demonstrates the complete preprocessing pipeline workflow.
Run this script to see the pipeline in action with the Titanic dataset.
"""

import pandas as pd
import numpy as np
from src.preprocessing import run_pipeline, DataPreprocessor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')


def download_titanic_dataset():
    """
    Download Titanic dataset from seaborn repository.
    """
    print("Downloading Titanic dataset...")
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
    df = pd.read_csv(url)
    df.to_csv('data/raw/titanic.csv', index=False)
    print(f"✅ Dataset saved: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def main():
    print("="*70)
    print("WEEK 2: REUSABLE DATA PREPROCESSING PIPELINE")
    print("="*70)
    
    # Step 1: Load data
    print("\n[STEP 1] Loading Titanic dataset...")
    try:
        df = pd.read_csv('data/raw/titanic.csv')
    except FileNotFoundError:
        print("  Dataset not found locally. Downloading...")
        df = download_titanic_dataset()
    
    print(f"  Shape: {df.shape}")
    print(f"  Missing values:\n{df.isnull().sum()}")
    
    # Step 2: Prepare features and target
    print("\n[STEP 2] Preparing features and target...")
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    print(f"  Features shape: {X.shape}")
    print(f"  Target shape: {y.shape}")
    print(f"  Numerical features: {X.select_dtypes(include=[np.number]).columns.tolist()}")
    print(f"  Categorical features: {X.select_dtypes(include=['object']).columns.tolist()}")
    
    # Step 3: Run preprocessing pipeline
    print("\n[STEP 3] Running preprocessing pipeline...")
    print("  - Splitting data (prevents data leakage)")
    print("  - Imputing missing values (mean for numerical, most_frequent for categorical)")
    print("  - Encoding categorical variables (OneHotEncoder)")
    print("  - Scaling numerical features (StandardScaler)")
    
    X_train, X_test, y_train, y_test = run_pipeline(
        X, y,
        test_size=0.2,
        imputation_strategy='mean',
        random_state=42
    )
    
    print(f"\n  ✅ Pipeline executed successfully!")
    print(f"  Train set: {X_train.shape}")
    print(f"  Test set: {X_test.shape}")
    print(f"  Target distribution (train):")
    print(f"    - Survived (1): {(y_train == 1).sum()}")
    print(f"    - Did not survive (0): {(y_train == 0).sum()}")
    
    # Step 4: Train a validation model
    print("\n[STEP 4] Training validation model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"  Model: Random Forest (100 estimators)")
    print(f"  \n  Performance Metrics:")
    print(f"    - Accuracy:  {accuracy:.4f}")
    print(f"    - Precision: {precision:.4f}")
    print(f"    - Recall:    {recall:.4f}")
    print(f"    - F1 Score:  {f1:.4f}")
    
    # Step 5: Save results
    print("\n[STEP 5] Saving results...")
    results_df = pd.DataFrame({
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],
        'Value': [accuracy, precision, recall, f1]
    })
    results_df.to_csv('results/pipeline_metrics.csv', index=False)
    print(f"  ✅ Saved to: results/pipeline_metrics.csv")
    
    # Save sample preprocessed data
    sample_data = pd.DataFrame(X_train[:100])  # First 100 rows
    sample_data.to_csv('results/sample_processed_data.csv', index=False)
    print(f"  ✅ Saved sample data to: results/sample_processed_data.csv")
    
    # Final summary
    print("\n" + "="*70)
    print("✅ PIPELINE EXECUTION COMPLETE")
    print("="*70)
    print("\nKey Takeaways:")
    print("  1. The pipeline successfully cleaned and preprocessed the data")
    print("  2. Missing values were imputed using statistical measures")
    print("  3. Categorical variables were one-hot encoded")
    print("  4. Numerical features were standardized for ML models")
    print("  5. The model achieved reasonable performance on the test set")
    print("\nNext Steps:")
    print("  - Try different imputation strategies: 'median', 'most_frequent'")
    print("  - Adjust the test_size parameter")
    print("  - Test with your own datasets")
    print("  - Deploy to Google Colab (see notebooks/COLAB_SETUP_GUIDE.md)")
    print("="*70)


if __name__ == "__main__":
    main()
