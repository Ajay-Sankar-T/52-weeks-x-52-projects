# Week 2: Preprocessing Pipeline - Colab Setup Guide

## Quick Start in Google Colab (No Local Setup Required!)

### Step 1: Open this notebook in Colab
1. Go to https://colab.research.google.com
2. Click **GitHub** tab
3. Paste: `Ajay-Sankar-T/52-weeks-x-52-projects`
4. Select `week-2` from the search results
5. Open this guide in a notebook

### Step 2: Clone the repo in Colab

```python
# Clone the repository
!git clone https://github.com/Ajay-Sankar-T/52-weeks-x-52-projects.git
%cd 52-weeks-x-52-projects/week-2
```

### Step 3: Install dependencies

```python
!pip install -r requirements.txt
```

### Step 4: Download Titanic dataset

```python
import pandas as pd
import numpy as np

# Download Titanic dataset from seaborn
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df.to_csv('data/raw/titanic.csv', index=False)

print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMissing values:\n{df.isnull().sum()}")
```

### Step 5: Run the preprocessing pipeline

```python
import sys
sys.path.insert(0, '/content/52-weeks-x-52-projects')

from week_2.src.preprocessing import run_pipeline
import pandas as pd

# Load data
df = pd.read_csv('data/raw/titanic.csv')

# Prepare features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Run the pipeline
X_train, X_test, y_train, y_test = run_pipeline(
    X, y, 
    test_size=0.2,
    imputation_strategy='mean',
    random_state=42
)

print(f"✅ Pipeline executed successfully!")
print(f"\nTrain shape: {X_train.shape}")
print(f"Test shape: {X_test.shape}")
print(f"Target distribution in train: {y_train.value_counts().to_dict()}")
```

### Step 6: Quick Model Validation

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Train a simple model to validate pipeline
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Model Performance:")
print(f"  Accuracy:  {accuracy:.4f}")
print(f"  Precision: {precision:.4f}")
print(f"  Recall:    {recall:.4f}")
```

### Step 7: Explore the preprocessed data

```python
import matplotlib.pyplot as plt

# Check distribution of features
plt.figure(figsize=(12, 6))
plt.hist(X_train[:, 0], bins=50, alpha=0.7)
plt.xlabel('First Feature (Scaled)')
plt.ylabel('Frequency')
plt.title('Distribution of First Feature After Preprocessing')
plt.show()

print(f"\n✅ All preprocessing steps completed successfully!")
print(f"\nFeature matrix shape: {X_train.shape}")
print(f"Number of features after encoding: {X_train.shape[1]}")
```

## Understanding the Pipeline

The `run_pipeline()` function does the following:
1. **Splits data** (prevents data leakage)
2. **Imputes missing values** (mean/median/mode for numerical, most_frequent for categorical)
3. **Encodes categorical variables** (OneHotEncoder)
4. **Scales numerical features** (StandardScaler)
5. **Returns** X_train, X_test, y_train, y_test ready for modeling

## Troubleshooting

- **Import error?** Make sure you ran the `sys.path.insert()` step
- **File not found?** Check that you're in `/content/52-weeks-x-52-projects/week-2`
- **Git error?** Run `!pip install gitpython` first

## Further Exploration

Try modifying the pipeline:
- Change `imputation_strategy` to `'median'` or `'most_frequent'`
- Adjust `test_size` to 0.15 or 0.25
- Create your own dataset and test the pipeline

## Next Steps

1. Save your Colab notebook
2. Run this with different datasets
3. Create a reusable data pipeline for future projects!
