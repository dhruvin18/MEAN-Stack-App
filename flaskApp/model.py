import pickle
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

vectorizer =pickle.load(open('./TFIDFvectorizer.pickle', 'rb'))  

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
