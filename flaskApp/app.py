from flask import Flask
from flask import jsonify
from flask import request
from preprocess import preProcess

app=Flask(__name__)

data='Dhruvin is tring flask'

@app.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'data':data})

@app.route('/pre_process',methods=['POST'])
def get_data():
    data=request.get_json()
    print(data['data'])
    final=preProcess(data['data'])
    return jsonify({'data':final})
 
if __name__== '__main__':
    app.run(debug=True)

