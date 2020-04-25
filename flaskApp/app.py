from flask import Flask
from flask import jsonify
from flask import request
from preprocess import preProcess

app=Flask(__name__)

# data=open('../Dataset/dataset_bombay/AakifAteequeNachanVTheStateOfMaharashtra.txt', 'r', encoding="utf8", errors="ignore")

@app.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'data':data})

@app.route('/pre_process',methods=['POST'])
def get_data():
    data=request.get_json()
    final=preProcess(data['data'])
    return jsonify({'data':final})
 
if __name__== '__main__':
    app.run(debug=True)

