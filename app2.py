import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app2=Flask(__name__)
app=app2

#load the files
standardScaler=pickle.load(open("normalize.pkl","rb"))
model=pickle.load(open("cancer_model.pkl","rb"))

#HOMEGAE ROUTE
@app.route('/')
def index():
    return render_template('index.html')

#NEXTpageroute
@app.route("/predictdata",methods=['POST','GET'])
def datapoint():
    if request.method=='POST':
        radius=float(request.form.get('r'))
        compactness_mean=float(request.form.get('cm'))
        concave_points_mean=float(request.form.get('cpm'))
        symmetry_mean=float(request.form.get('sm'))
        fractal_mean=float(request.form.get('fractal'))
        symmetry_worst=float(request.form.get('sw'))

        data=standardScaler.transform([[radius,compactness_mean,concave_points_mean,symmetry_mean,fractal_mean,symmetry_worst]])
        result=model.predict(data)

        return render_template('predict.html',result=result[0])

    
    else:
        return render_template('predict.html',result=None)
    



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)