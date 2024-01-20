from flask import Flask, render_template, request
from helpers.transform import *
import joblib

app = Flask(__name__, template_folder='templates')

model = joblib.load('model.h5')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    all_data = request.args
    BMI = transform_bmi(int(all_data['BMI']))
    Smoking = transform_yes_no(all_data['Smoking'])
    AlcoholDrinking = transform_yes_no(all_data["AlcoholDrinking"])
    Stroke = transform_yes_no(all_data['Stroke'])
    PhysicalHealth = transform_mental_physical(int(all_data['PhysicalHealth']))
    MentalHealth = transform_mental_physical(int(all_data['MentalHealth']))
    DiffWalking = transform_yes_no(all_data["DiffWalking"])
    Sex = transform_gender(all_data["Sex"])
    AgeCategory = transform_age(int(all_data['AgeCategory']))
    Diabetic = transform_diabetes(all_data['Diabetic'])
    PhysicalActivity = transform_yes_no(all_data['PhysicalActivity'])
    GenHealth = transform_GenHealth(all_data['GenHealth'])
    SleepTime = transform_sleepTime(int(all_data['SleepTime']))
    Asthma = transform_yes_no(all_data["Asthma"])
    KidneyDisease = all_data["KidneyDisease"]
    SkinCancer = transform_yes_no(all_data["SkinCancer"])
    x = [[BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex,
          AgeCategory, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer]]
    pred = model.predict(x)
    if pred == 0:
        x = "negative case"
    else:
        x = "positive case!"

    return render_template('index-2.html', prediction=str(x))


if __name__ == '__main__':
    app.run(debug=True)
