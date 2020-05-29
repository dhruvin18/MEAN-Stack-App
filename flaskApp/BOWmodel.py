# Reading cleaned dataset
import pandas as pd
df = pd.read_csv('./cleaned_dataset.csv')

# Splitting the dataset into train and test sets
X = df.loc[:,'Judgement'].values
y = df.loc[:,'label'].values
from sklearn.model_selection import train_test_split
traindf = pd.read_csv('./train.csv')
testdf = pd.read_csv('./test.csv')
X_train = traindf.loc[:,'Judgement'].values
X_test = testdf.loc[:,'Judgement'].values

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

cv= CountVectorizer(ngram_range=(1,3), max_features=5000)
X_train_counts= cv.fit_transform(X_train)
tfidf_transformer = TfidfTransformer(use_idf=False)
train_vectors = tfidf_transformer.fit_transform(X_train_counts)
# X_test_counts= cv.transform(X_test)
# test_vectors = tfidf_transformer.transform(X_test_counts)

from sklearn import preprocessing
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_mabs= max_abs_scaler.fit_transform(train_vectors)
# X_test_mabs= max_abs_scaler.transform(test_vectors)

import pickle

SVMloaded_model = pickle.load(open('./BOWSVM_model.sav', 'rb'))
NBloaded_model = pickle.load(open('./BOWNB_model.sav', 'rb'))
KNNloaded_model = pickle.load(open('./BOWKNN_model.sav', 'rb'))
LRloaded_model = pickle.load(open('./BOWLR_model.sav', 'rb'))
RFloaded_model = pickle.load(open('./BOWRF_model.sav', 'rb'))

def predictclass(data):
    case=[]
    case.append(data)
    X_pred=cv.transform(case)
    test_pred_vector= tfidf_transformer.transform(X_pred)
    X_pred_mabs = max_abs_scaler.transform(test_pred_vector)
    svm_predict_label = SVMloaded_model.predict(X_pred_mabs)
    nb_predict_label = NBloaded_model.predict(test_pred_vector)
    knn_predict_label = KNNloaded_model.predict(X_pred_mabs)
    lr_predict_label = LRloaded_model.predict(X_pred_mabs)
    rf_predict_label = RFloaded_model.predict(test_pred_vector)
    return svm_predict_label.item(0),nb_predict_label.item(0),knn_predict_label.item(0),lr_predict_label.item(0),rf_predict_label.item(0)


