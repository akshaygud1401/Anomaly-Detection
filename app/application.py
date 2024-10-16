from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('../app/bestHGBT.joblib')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        prediction = None
        cols = ["std_local_source_degrees", 
                "avg_global_source_degrees",
                "max_global_dest_degrees",
                "max_global_source_degrees",
                "std_global_source_degrees",
                "min_global_source_degrees",
                "avg_global_dest_degrees",
                "n_connections",
                "min_global_dest_degrees"]
        features = [request.form.get(x) for x in cols]
        X = dict(zip(cols, features))
        pred = round(model.predict_proba(pd.DataFrame(X, index=[0]))[0][1], 2)
        if pred > 0.5:
            prediction = 'this behavior is classified as anomalous'
        else:
            prediction = 'this behavior is not classified as anomalous' 
        return render_template('index.html', prediction=f'Probability of anomaly is {pred}; {prediction}')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8989)