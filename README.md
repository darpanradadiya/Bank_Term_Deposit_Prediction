# Bank Term Deposit Prediction

## Project Overview
This project helps a Portuguese banking institution predict whether clients will subscribe to term deposits based on direct marketing campaigns conducted through phone calls. The project implements and compares various machine learning models to identify which performs best for this prediction task.

## Objectives
1. **Identify Key Factors**: Determine which client attributes (e.g., age, job type, marital status) most influence term deposit subscriptions
2. **Data Analysis and Exploration**: Gain insights into client characteristics and analyze relationships between variables
3. **Predictive Modeling**: Build models to predict term deposit subscriptions
4. **Model Evaluation**: Compare different models in terms of accuracy, precision, recall, and F1 score

## Dataset Description
- **Source**: UCI Machine Learning Repository
- **Records**: 45,211 rows
- **Features**: 17 attributes (7 numerical, 10 categorical)
- **Target Variable**: Whether the client subscribed to a term deposit ("yes" or "no")
- **Class Imbalance**: 88.3% "no" responses, 11.7% "yes" responses

### Key Features
- **Numerical Attributes**: age, balance, duration of last contact, campaign, previous contact
- **Categorical Attributes**: job type, marital status, education, loan status, contact type

## Methodology
1. **Data Cleaning and Preprocessing**:
   - Checking for missing values and duplicates
   - Treating outliers using IQR method
   - One-hot encoding for categorical variables
   - Standardizing numerical features

2. **Exploratory Data Analysis**:
   - Distribution analysis of numerical features
   - Examination of categorical variables distribution
   - Correlation analysis between variables

3. **Baseline Model Development**:
   - Logistic Regression
   - Decision Tree
   - Random Forest

4. **Hyperparameter Tuning**:
   - Optimizing model parameters using RandomizedSearchCV
   - Evaluation with cross-validation

## Key Findings
1. **Feature Importance**:
   - Duration of last contact is the most influential predictor across all models
   - Age, balance, and day of contact are also significant factors
   - Successful previous marketing campaigns strongly correlate with new subscriptions

2. **Model Performance**:
   | Model               | Accuracy | Precision | Recall  | F1 Score |
   |---------------------|----------|-----------|---------|----------|
   | Logistic Regression | 89.76%   | 64.01%    | 34.56%  | 44.88%   |
   | Decision Tree       | 87.13%   | 46.62%    | 46.20%  | 46.41%   |
   | Random Forest       | 90.15%   | 66.13%    | 37.58%  | 47.93%   |

3. **Hypertuned Models**:
   | Model               | Accuracy | Precision | Recall  | F1 Score |
   |---------------------|----------|-----------|---------|----------|
   | Logistic Regression | 89.76%   | 64.05%    | 34.46%  | 44.82%   |
   | Decision Tree       | 87.96%   | 50.11%    | 43.08%  | 46.33%   |
   | Random Forest       | 90.01%   | 65.21%    | 36.94%  | 47.16%   |

## Conclusion
The Random Forest model emerged as the best performer, achieving the highest accuracy (90.15%) and F1 score. Interestingly, hyperparameter tuning did not significantly improve model performance, suggesting the default settings were already well-suited for this dataset.

The analysis revealed that longer conversations with clients, higher account balances, and successful previous engagements are strong indicators of term deposit subscriptions. These insights can help the bank optimize its marketing strategies and target the most promising leads.


## Setup and Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/bank-term-deposit-prediction.git
   cd bank-term-deposit-prediction
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
- To run data preprocessing:
  ```
  python src/data_cleaning.py
  ```

- To train and evaluate baseline models:
  ```
  python src/baseline_models.py
  ```

- To train and evaluate tuned models:
  ```
  python src/tuned_models.py
  ```

## Future Work
- Implement more advanced algorithms (XGBoost, Neural Networks)
- Address class imbalance using techniques like SMOTE
- Feature engineering to improve model performance
- Develop an interactive dashboard for real-time predictions

## Contributors
- Darpan Radadiya


## Acknowledgments
- UCI Machine Learning Repository for providing the dataset
- The bank for the collaboration opportunity