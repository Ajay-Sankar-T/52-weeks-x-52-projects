
# Week 2: From Raw Dataset → Clean ML-Ready Pipeline

## Problem Statement

Build a reusable, end-to-end data preprocessing pipeline that turns messy real-world data into a model-ready dataset. This project demonstrates the foundation of professional ML work: understanding, cleaning, and transforming raw data.

## 🎯 Objectives

- **Exploratory Data Analysis (EDA)**: Understand data structure, distributions, and anomalies
- **Preprocessing Pipeline**: Build reusable, scalable data transformation code
- **Feature Engineering**: Handle missing values, outliers, and categorical variables
- **Model Validation**: Train-test split and basic model evaluation

## 📦 Project Scope

### Input
A messy real-world dataset with:
- Missing values
- Categorical variables
- Outliers
- Inconsistent data types

### Output
- Cleaned, processed dataset
- Reusable preprocessing code (sklearn Pipeline)
- Data quality report
- Train-test split ready for modeling

## 🔧 What's Included

### 1. **Exploratory Data Analysis** (`notebooks/eda.ipynb`)
- Data shape and data types
- Missing value patterns
- Statistical distributions
- Correlation analysis
- Outlier detection

### 2. **Preprocessing Pipeline** (`src/preprocessing.py`)
```python
class DataPreprocessor:
    """Reusable preprocessing pipeline using sklearn."""
    
    - Handle missing values (imputation strategies)
    - Encode categorical variables (OneHot / Ordinal)
    - Scale numerical features (StandardScaler / MinMaxScaler)
    - Detect and handle outliers
    - Train-test split
```

### 3. **Requirements** (`requirements.txt`)
- pandas, numpy: Data manipulation
- scikit-learn: ML preprocessing & modeling
- matplotlib, seaborn: Visualization
- jupyter, ipython: Notebooks

### 4. **Folder Structure**
```
week-2/
├── data/
│   ├── raw/              # Original messy data
│   └── processed/        # Cleaned, transformed data
├── notebooks/
│   └── eda.ipynb        # Exploratory analysis
├── src/
│   └── preprocessing.py  # Reusable pipeline
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## 🧠 Key Concepts Demonstrated

✅ **EDA**: Understand data before modeling  
✅ **Feature Scaling**: Normalize numerical features  
✅ **Categorical Encoding**: Transform text to numbers  
✅ **Missing Data Strategy**: Imputation vs deletion  
✅ **Train-Test Split**: Prevent data leakage  
✅ **Reproducibility**: Reusable, documented code  
✅ **Sklearn Pipelines**: Professional ML best practices  

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run EDA Notebook
```bash
jupyter notebook notebooks/eda.ipynb
```

### 3. Use the Preprocessing Pipeline
```python
from src.preprocessing import DataPreprocessor
import pandas as pd

# Load data
df = pd.read_csv('data/raw/your_dataset.csv')

# Initialize preprocessor
preprocessor = DataPreprocessor(test_size=0.2, random_state=42)

# Split data
X_train, X_test, y_train, y_test = preprocessor.split_data(X, y)

# Fit and transform
X_train_processed = preprocessor.fit_transform(X_train, y_train)
X_test_processed = preprocessor.transform(X_test)
```

## 📊 Expected Results

- ✅ Clean dataset with no missing values
- ✅ Properly scaled numerical features
- ✅ Encoded categorical variables
- ✅ Train-test split (80-20)
- ✅ Documented EDA notebook
- ✅ Baseline model evaluation

## 🎓 Learnings

1. **Data Quality Matters**: 80% of ML work is preprocessing
2. **Reproducibility**: Use pipelines for consistent results
3. **Feature Engineering**: Domain knowledge + data understanding
4. **Train-Test Split**: Prevent overfitting from day one
5. **Documentation**: Code that works + code others understand

## 📚 Resources Used

- [scikit-learn Pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [Handling Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Feature Scaling](https://scikit-learn.org/stable/modules/preprocessing.html)

## 🔗 Related Topics

- Week 1: System Setup & Repository Structure
- Week 3: Model Training & Evaluation (coming next)
- Week 4+: Advanced ML techniques

---

**Status**: 🟡 In Progress  
**Started**: Jan 9, 2026  

**Completed**: Jan 14, 2026
**Language**: Python 3.8+
**Framework**: scikit-learn, pandas, jupyter (Colab)

## ✅ v1 Completion Status

**DONE**: Full end-to-end preprocessing pipeline

### Pipeline Execution Results
- **Dataset**: Titanic (891 samples, 15 raw features)
- **Train-Test Split**: 712 training, 179 testing samples
- **Missing Value Handling**: Imputed mean for numeric, mode for categorical
- **Categorical Encoding**: OneHotEncoder → 28 final features
- **Numerical Scaling**: StandardScaler applied
- **Model Training**: RandomForest classifier - **100% accuracy** on test set
- **Implementation**: Google Colab notebook (fully reproducible)

### Key Achievements
✅ Download & load real dataset  
✅ Complete preprocessing pipeline (7 steps)  
✅ Train-test split (80-20)  
✅ Handle missing values (mean imputation)  
✅ Encode categorical variables (OneHotEncoder)  
✅ Scale numerical features (StandardScaler)  
✅ Train model and evaluate performance  
✅ 100% accuracy on test set  

### How to Access
1. **Colab Notebook**: `notebooks/exploration.ipynb` - Full pipeline with outputs
2. **Run Locally**: Clone repo, install requirements, adapt notebook code
**Language**: Python 3.8+  
**Framework**: scikit-learn, pandas
