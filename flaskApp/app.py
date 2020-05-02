from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from preprocess import preProcess
from model import predict_label
from flask import send_file
from flask import request

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
    data=preProcess(data['data'])
    final=predict_label(data)
    print(final)
    return final

@app.route('/filenames',methods=['POST'])
def get_filenames():
    filename1='AmrishTrivediAliasNikkiVStateOfUP.txt'
    link1= 'http://localhost:5000/download/'+filename1
    filename2='BhagwanDeenVStateOfUP.txt'
    link2 = 'http://localhost:5000/download/'+filename2
    filename3='BholaRamlakhanGuptaVStateOfMaharashtra.txt'
    return jsonify({"filenames":[{"name": filename1, "link": link1 }, {"name": filename2, "link": link2 }]})

@app.route('/download/<name>', methods=['GET'])
def download(name):
    file='./../server/Dataset/'+name
    return send_file(file, as_attachment=True)
    
if __name__== '__main__':
    app.run(debug=True)

