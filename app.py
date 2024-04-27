from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_cors import CORS
from regression import regression
from classification import classification
from prediciton import pred
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/crime2001_2012.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crime_output', methods=['POST'])
def suggest_plans():
    input_state = request.form['input_state']
    input_district = request.form['input_district']
    input_year = request.form['input_year']
    input_period = request.form['input_period']

    crime_types, predicted_rates = regression(data, input_state, input_district, input_year)
    class_result = classification(data, input_state, input_district, input_year)

    model,future = pred(data, input_period)

    forecast = model.forecast(future)

    fig2 = model.plot_components(forecast)
    plt.show()
    
    return render_template('forecast.html', crime_type = crime_types, predicted_rates = predicted_rates, class_result = 
                           class_result)

if __name__ == '__main__':
    app.run(debug=True)