from flask import Flask,request,render_template
from utils import body_checkup_charges



app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data',methods=['POST','GET'])
def get_data():
    data=request.form
    class_object=body_checkup_charges(data)
    result = class_object.charges_prediction()

    return render_template('index.html',prediction=result)

if __name__=='__main__':
    app.run(host='localhost',debug = True)