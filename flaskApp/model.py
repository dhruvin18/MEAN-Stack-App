import pickle
from flask import jsonify
import pandas as pd

svmfilename = 'svm_model.sav'
nbfilename = 'nb_model.sav'
knnfilename = 'knn_model.sav'
lrfilename = 'lr_model.sav'
rffilename = 'rf_model.sav'
SVMloaded_model = pickle.load(open(svmfilename, 'rb'))
NBloaded_model = pickle.load(open(nbfilename, 'rb'))
KNNloaded_model = pickle.load(open(knnfilename, 'rb'))
LRloaded_model = pickle.load(open(lrfilename, 'rb'))
RFloaded_model = pickle.load(open(rffilename, 'rb'))

#path = '/content/drive/My Drive/BE PROJECT/Lawgical Final/LabelledDataset/'
traindf = pd.read_csv('./train.csv')
testdf = pd.read_csv('./test.csv')
X_train = traindf.loc[:,'Judgement'].values
X_test = testdf.loc[:,'Judgement'].values

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(X_train)
def predict_label(data):
    case=[]
    case.append(data)
    vectorcase=vectorizer.transform(case)
    svm_predict_label = SVMloaded_model.predict(vectorcase)
    nb_predict_label = NBloaded_model.predict(vectorcase)
    knn_predict_label = KNNloaded_model.predict(vectorcase)
    lr_predict_label = LRloaded_model.predict(vectorcase)
    rf_predict_label = RFloaded_model.predict(vectorcase)
    return svm_predict_label.item(0),nb_predict_label.item(0),knn_predict_label.item(0),lr_predict_label.item(0),rf_predict_label.item(0)
