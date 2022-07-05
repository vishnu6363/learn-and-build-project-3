from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
app=Flask(__name__)
pickle_in=open('clsifier.pkl','rb')
clasifier=pickle.load(pickle_in) 
@app.route('/')
def welcome():
    return "welecome All"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=clasifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is "+str(prediction) 

@app.route('/predict_file',methods=['POST'])
def note_file():
    df_test=pd.read_csv(request.files.get('file'))
    prediction=clasifier.predict(df_test)
    return "The predicted value is "+str(prediction)
    




if(__name__=='__main__'):
    app.run() 