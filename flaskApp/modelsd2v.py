from gensim.models.doc2vec import Doc2Vec, TaggedDocument  
from nltk.tokenize import word_tokenize
import multiprocessing
from sklearn import utils
import glob
import nltk
import pandas as pd
import string
import numpy as np
from datetime import datetime
from flask import jsonify
import pickle

print(datetime.now())
model =Doc2Vec.load('d2vec.model')
# print(type(model))
LRloaded_model = pickle.load(open('./d2vlr_model.sav', 'rb'))
RFloaded_model = pickle.load(open('./d2vrf_model.sav', 'rb'))
SVMloaded_model = pickle.load(open('./d2vsvm_model.sav', 'rb'))
print(datetime.now())
print('model Loaded')

def vec_for_learning(model, tagged_docs):
    sents = tagged_docs 
    targets, regressors = zip(*[(doc.tags[0], model.infer_vector(doc.words, steps=20)) for doc in sents])
    return targets, regressors

# test = pd.read_csv('./test.csv')
# tagged_data_test = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in test.iterrows()]
# y_test,X_test= vec_for_learning(model, tagged_data)


# print(y_test[10:40])
def predictD2Vclass(data):
    tagged_data_predict = [TaggedDocument(words=word_tokenize(data),tags= [str(0)])]
    y_pred,X_pred=vec_for_learning(model,tagged_data_predict)
    lr_predict_label = LRloaded_model.predict(X_pred)
    rf_predict_label = RFloaded_model.predict(X_pred)
    svm_predict_label = SVMloaded_model.predict(X_pred)
    return svm_predict_label.item(0),lr_predict_label.item(0),rf_predict_label.item(0)

