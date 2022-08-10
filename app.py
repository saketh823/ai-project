# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 16:54:30 2022

@author: saketh
"""
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM
import tensorflow as tf
from keras.models import load_model

app=Flask(__name__)
#model = tf.keras.models.load_model("model.h5","rb")
model=load_model("model.h5")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [[[x for x in request.form.values()]]]
    print(int_features)
    
    
    final_features = [np.array(int_features)]
    print("\n\n\n\n\n\n",final_features)
    prediction = model.predict(final_features)

    
    return render_template('index.html', prediction_text='The predicted price of Bitcoin is {}'.format(str(prediction)))



if __name__=='__main__':
    app.run()