from flask import Flask,render_template,request
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import numpy as np
import pickle

app=Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def get_result():
    poly=pickle.load(open('poly.pkl','rb'))
    model= pickle.load(open('model.pkl','rb'))
    query=[[float(request.form['Experience'])]]
    x_query=poly.transform(query)
    sal=model.predict(x_query)
    #sal=250000
    return 'dear ' +request.form["Name"]+ ' Your predicted salary after' +request.form["Experience"]+ ' year is' +str(sal);
if __name__=='__main__':

    app.run(debug=True)
