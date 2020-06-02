from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from preprocess import preProcess
from model import predict_label
from modelsd2v import predictD2Vclass
from BOWmodel import predictclass
from flask import send_file
from flask import request

app=Flask(__name__)
CORS(app)
# data=open('../Dataset/dataset_bombay/AakifAteequeNachanVTheStateOfMaharashtra.txt', 'r', encoding="utf8", errors="ignore")

@app.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'data':data})

@app.route('/pre_process',methods=['POST'])
def get_cleaned_data():
    data=request.get_json()
    final=preProcess(data['data'])
    return jsonify({'data':final})

@app.route('/predict_class', methods=['POST'])
def get_class():
    data=request.get_json()
    data=preProcess(data['data'])
    svm,nb,knn,lr,rf=predict_label(data)
    k,l,m,n,f=predictD2Vclass(data)
    a,b,c,d,e=predictclass(data)
    positive=(int(svm)+int(nb)+int(knn)+int(lr)+int(rf)+int(k)+int(l)+int(m)+int(n)+int(a)+int(b)+int(c)+int(d)+int(e))
    return jsonify({"case":data, "SVM":svm, "Naive Bayes": nb, "k Nearest Neighbour": knn,"Logistic Regression": lr, "Random Forest": rf , "D2VSVM": k, "D2VLR": l, "D2VRf": m, "D2VKNN":n,"BOWRF": e, "BOWSVM": a, "BOWNB": b, "BOWKNN": c, "BOWLR": d, "filenames": f, "cases": positive})

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
    file='./../../Dataset/dataset/'+name
    return send_file(file, as_attachment=True)
    
if __name__== '__main__':
    app.run(debug=False)

