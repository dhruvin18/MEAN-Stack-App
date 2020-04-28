from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from preprocess import preProcess
from model import predict_label

app=Flask(__name__)
CORS(app)
# data=open('../Dataset/dataset_bombay/AakifAteequeNachanVTheStateOfMaharashtra.txt', 'r', encoding="utf8", errors="ignore")

@app.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'data':data})

@app.route('/pre_process',methods=['POST'])
def get_cleanede_data():
    data=request.get_json()
    final=preProcess(data['data'])
    return jsonify({'data':final})

@app.route('/predict_class', methods=['POST'])
def get_class():
    data=request.get_json()
    final=predict_label(data['data'])
    return final


if __name__== '__main__':
    app.run(debug=True)

