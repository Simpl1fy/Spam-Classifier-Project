from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        cd = CustomData(text=request.form.get('sms-text'))
        ser = cd.get_data_as_series()
        print(ser)
        print("Before Prediction")
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        result = predict_pipeline.predict(ser)
        output = result[0]
        print('Prediction Completed')
        print(output)
        if (output == 1):
            res = "a spam✔️"
        else:
            res = "is not a spam❌"
        print(res)
        return render_template('index.html', output=res)

if __name__ == "__main__":
    app.run(debug=True)