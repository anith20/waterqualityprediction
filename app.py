from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

 # Load the trained model
with open('model (3).pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        ammonia = float(request.form['ammonia'])
        aluminium = float(request.form['aluminium'])
        arsenic = float(request.form['arsenic'])
        barium = float(request.form['barium'])
        cadmium = float(request.form['cadmium'])
        chloramine = float(request.form['chloramine'])
        chromium = float(request.form['chromium'])
        copper = float(request.form['copper'])
        flouride = float(request.form['flouride'])
        bacteria = float(request.form['bacteria'])
        viruses = float(request.form['viruses'])
        lead = float(request.form['lead'])
        nitrates = float(request.form['nitrates'])
        nitrites = float(request.form['nitrites'])
        mercury = float(request.form['mercury'])
        perchlorate = float(request.form['perchlorate'])
        radium = float(request.form['radium'])
        selenium = float(request.form['selenium'])
        silver = float(request.form['silver'])
        uranium = float(request.form['uranium'])

         # Create a feature vector
        input_features = np.array([[ ammonia,aluminium, arsenic, barium, cadmium, chloramine, chromium, copper,
                                    flouride, bacteria, viruses, lead, nitrates, nitrites, mercury,
                                    perchlorate, radium, selenium, silver, uranium]])

         # Make prediction using the loaded model
        prediction = model.predict(input_features)

         # Return the prediction result
        if prediction[0] == 0:
            return render_template('result.html', prediction_text='Water is not safe to drink')
        else:
            return render_template('result.html', prediction_text='Water is safe to drink')

if __name__ == '__main__':
    app.run(debug=True)


