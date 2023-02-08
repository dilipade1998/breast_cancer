from flask import Flask , render_template , jsonify ,request
from project_app.utils import Cancer_Prediction
import pickle
import json
import config

app=Flask(__name__)

@app.route("/") #home API

def base():
    return render_template("home.html")
    
@app.route("/predict",methods=["POST"])

def cancer():
    data = request.form 
    radius_mean = eval(data["radius_mean"])
    texture_mean = eval(data["texture_mean"])
    perimeter_mean = eval(data["perimeter_mean"])
    area_mean = eval(data["area_mean"])
    smoothness_mean = eval(data["smoothness_mean"])
    compactness_mean = eval(data["compactness_mean"])
    concavity_mean = eval(data["concavity_mean"])
    concave_points_mean = eval(data["concave_points_mean"])
    symmetry_mean = eval(data["symmetry_mean"])
    fractal_dimension_mean = eval(data["fractal_dimension_mean"])
    radius_se = eval(data["radius_se"])
    texture_se = eval(data["texture_se"])
    perimeter_se = eval(data["perimeter_se"])
    area_se = eval(data["area_se"])
    smoothness_se = eval(data["smoothness_se"])
    compactness_se = eval(data["compactness_se"])
    concavity_se = eval(data["concavity_se"])
    concave_points_se = eval(data["concave_points_se"])
    symmetry_se = eval(data["symmetry_se"])
    fractal_dimension_se = eval(data["fractal_dimension_se"])
    radius_worst = eval(data["radius_worst"])
    texture_worst = eval(data["texture_worst"])
    perimeter_worst = eval(data["perimeter_worst"])
    area_worst = eval(data["area_worst"])
    smoothness_worst = eval(data["smoothness_worst"])
    compactness_worst = eval(data["compactness_worst"])
    concavity_worst = eval(data["concavity_worst"])
    concave_points_worst = eval(data["concave_points_worst"])
    symmetry_worst = eval(data["symmetry_worst"])
    fractal_dimension_worst = eval(data["fractal_dimension_worst"])



    x=Cancer_Prediction(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, 
                concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, 
                texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, 
                symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst,
                smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst)
    final=x.prediction()
    M="Metastasis (M),Metastatic breast cancer is cancer that spreads to other organs in the body."
    if final == 1:
        return render_template("next.html",data=M)
    else:
        return render_template("next.html",data="Benign(non-cancerous)")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)