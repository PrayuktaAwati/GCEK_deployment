from flask import Flask, render_template,request
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def get_result():
	#use model.predict to predict salary
	#sal = 12000
	poly = pickle.load(open('Poly.pkl','rb'))
	model = pickle.load(open('model.pkl','rb'))
	query = [[float(request.form['text2'])]]
	X_query = poly.transform(query)
	sal = model.predict(X_query)
	
	return 'Dear '+request.form["text1"]+' Your predicted salary after ' + request.form["text2"]+' year experience is :'+str(sal)
	
	#return'Your Predicted Salary is 50000'
if __name__ == '__main__':
   app.run(debug=True)
