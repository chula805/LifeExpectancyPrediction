# Life Expectancy Prediction Application

This application uses machine learning models to predict life expectancy based on various input features. The models included in this application are Random Forest, XGBoost, CatBoost, and LightGBM regressors.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or higher)
- Flask
- NumPy
- Pandas
- Scikit-learn
- XGBoost
- CatBoost
- LightGBM

You can install the required Python libraries using the following command:

```
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/life-expectancy-prediction.git
```

2. Navigate to the project directory:

```
cd life-expectancy-prediction
```

3. Run the Flask application:

```
python app.py
```

The application should now be running locally on http://localhost:5000/.

## Usage

1. Open your web browser and go to http://localhost:5000/.
2. Enter the required input features (Adult Mortality, Alcohol, Percentage Expenditure, etc.).
3. Click on the "Predict" button to see the predicted life expectancy.

