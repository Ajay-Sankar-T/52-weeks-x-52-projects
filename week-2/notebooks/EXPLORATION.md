# Week 2 Data Preprocessing Pipeline - Exploration Notebook

## Overview
This is the working exploration and testing notebook for the Week 2 data preprocessing pipeline.

## Live Notebook (Google Colab)
**[Open in Colab](https://colab.research.google.com/drive/1d5nro4gaZ47XeRBKhKHfecQejN7wFKJ4)**

### Notebook Contents
- **Step 1**: Download Titanic dataset (891 samples, 15 features)
- **Step 2**: Prepare features and target variables
- **Step 3**: Train-test split (80-20) → 712 training, 179 test samples
- **Step 4**: Handle missing values → Mean imputation for numeric, Mode for categorical
- **Step 5**: Categorical variable encoding → OneHotEncoder → 28 final features
- **Step 6**: Numerical feature scaling → StandardScaler
- **Step 7**: Model training → RandomForest classifier

### Results
- **Accuracy**: 100% on test set
- **Final Feature Shape**: (712, 28) training, (179, 28) test
- **Preprocessing Pipeline**: Fully reusable and reproducible

## How to Use
1. Click the Colab link above to open the notebook
2. Run all cells sequentially (`Ctrl + F9` or Runtime > Run all)
3. The pipeline will execute end-to-end with full output visualization

## Technology Stack
- Python 3.8+
- Google Colab (free cloud GPU access)
- scikit-learn (preprocessing & modeling)
- pandas (data manipulation)
- numpy (numerical computing)

## Status
✅ **COMPLETE** - Full v1 pipeline working with 100% test accuracy
