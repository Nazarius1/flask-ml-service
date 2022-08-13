from flask import Flask, request, url_for, redirect, render_template, jsonify
import xgboost
import pandas as pd
import joblib


import numpy as np



app = Flask(__name__)
reg1 =joblib.load('Xgb.pkl')
cols = ['LSTAT','RM','PTRATIO','INDUS']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    print("predict requested")
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    print(data_unseen.dtypes)
    prediction = reg1.predict(data_unseen)

    return jsonify({'prediction' : prediction.tolist()})
    #return jsonify({"prediction":prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
