from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('log_model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("bladder.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output = prediction
    print(output)
    if output==str(1):
        return render_template('bladder.html',pred='Need to get an Incontinence CHECK!\n {}'.format(output),bhai="Need to get an Incontinence CHECK!")
    else:
        return render_template('bladder.html',pred='Safe from Incontinence\n  {}'.format(output),bhai="Safe from Incontinence")


if __name__ == '__main__':
    app.run(debug=True)