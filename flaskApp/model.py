svmfilename = 'svm_model.sav'
nbfilename = 'nb_model.sav'
knnfilename = 'knn_model.sav'
lrfilename = 'lr_model.sav'
rffilename = 'rf_model.sav'

from flask import jsonify
import pandas as pd
#path = '/content/drive/My Drive/BE PROJECT/Lawgical Final/LabelledDataset/'
traindf = pd.read_csv('./train.csv')
testdf = pd.read_csv('./test.csv')
X_train = traindf.loc[:,'Judgement'].values
X_test = testdf.loc[:,'Judgement'].values

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(X_train)
import pickle
def predict_label(data):
    case=[]
    case.append(data)
    vectorcase=vectorizer.transform(case)
    #predicted_label=svm.predict(vectorcase)
    loaded_model = pickle.load(open(svmfilename, 'rb'))
    svm_predict_label = loaded_model.predict(vectorcase)
    loaded_model = pickle.load(open(nbfilename, 'rb'))
    nb_predict_label = loaded_model.predict(vectorcase)
    loaded_model = pickle.load(open(knnfilename, 'rb'))
    knn_predict_label = loaded_model.predict(vectorcase)
    loaded_model = pickle.load(open(lrfilename, 'rb'))
    lr_predict_label = loaded_model.predict(vectorcase)
    loaded_model = pickle.load(open(rffilename, 'rb'))
    rf_predict_label = loaded_model.predict(vectorcase)
    return jsonify({"SVM": svm_predict_label.item(0) , "Naive Bayes": nb_predict_label.item(0), "k Nearest Neighbour": knn_predict_label.item(0), "Logistic Regression": lr_predict_label.item(0), "Random Forest": rf_predict_label.item(0)})