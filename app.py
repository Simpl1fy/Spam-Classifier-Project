from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, SMSPredictPipeline, EmailPredictPipeline
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/smsprediction', methods=['POST', 'GET'])
def sms_prediction():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        cd = CustomData(text=request.form.get("sms-text"))
        ser = cd.get_data_as_series()
        print(ser)
        print("Before Prediction")
        predict_pipeline = SMSPredictPipeline()
        print("Mid Prediction")
        result = predict_pipeline.predict(ser)
        output = result[0]
        print('Prediction Completed')
        print(output)
        if (output == 1):
            sms_res = "a spam✔️"
        else:
            sms_res = "is not a spam❌"
        print(sms_res)
        return render_template('index.html', sms_output=sms_res)


@app.route('/emailprediction', methods=['POST', 'GET'])
def email_prediction():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        cd = CustomData(text=request.form.get("mail-text"))
        ser = cd.get_data_as_series()
        print(ser)
        print("Before Prediction")
        predict_pipeline = EmailPredictPipeline()
        print("Mid Prediction")
        result = predict_pipeline.predict(ser)
        output = result[0]
        print('Prediction Completed')
        print(output)
        if (output == 1):
            email_res = "a spam✔️"
        else:
            email_res = "is not a spam❌"
        print(email_res)
        return render_template('index.html', email_output=email_res)


if __name__ == "__main__":
    app.run(debug=True)