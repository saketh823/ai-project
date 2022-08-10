# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:54:30 2022

@author: saketh
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM


app=Flask(__name__)
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    
    return render_template('index.html', prediction_text='The flower belong to species {}'.format(str(prediction)))
    


if __name__=='__main__':
    app.run()