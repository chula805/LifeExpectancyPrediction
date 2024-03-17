from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__, template_folder='template')

# Load the trained model
model = joblib.load("best_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        country = request.form['country']
        year = int(request.form['year'])
        status = request.form['status']
        adultMortality = float(request.form['adultMortality'])
        infantdeaths = float(request.form['infantdeaths'])
        alcohol = float(request.form['alcohol'])
        bmi = float(request.form['bmi'])
        underfivedeaths = float(request.form['underfivedeaths'])
        polio = float(request.form['polio'])
        hivaids = float(request.form['hivaids'])
        gdp = float(request.form['gdp'])
        population = float(request.form['population'])
        resources = float(request.form['resources'])

        # Transform input features
        features = np.array([year, adultMortality, infantdeaths, alcohol, bmi, underfivedeaths, 
                             polio,hivaids, gdp, population, resources]).reshape(1, -1)
        prediction = model.predict(features)

        return render_template('index.html', lifeExpectancy=prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
