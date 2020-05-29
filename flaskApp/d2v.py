from gensim.models.doc2vec import Doc2Vec, TaggedDocument  
from nltk.tokenize import word_tokenize
from tqdm import tqdm
import multiprocessing
from sklearn import utils
import glob
import nltk
from nltk.tokenize import RegexpTokenizer
from spacy.lang.en import English
from spacy import displacy
import en_core_web_sm
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import string
import numpy as np

data = dict()
filenames=list()
cleaned_text=list()
label=list()

train = pd.read_csv('./train.csv')
# test = pd.read_csv('./test.csv')
print(train.shape)

# tagged_data = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in train.iterrows()]
# tagged_data_test = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in test.iterrows()]
tagged_data = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(i)]) for i, _d in train.iterrows()]
# tagged_data_test = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(i)]) for i, _d in test.iterrows()]

print(len(tagged_data))
# instantiate a Doc2Vec model with following parameters
max_epochs = 10
vec_size = 10000
alpha = 0.050


model = Doc2Vec(vector_size=vec_size, #Dimensionality of the feature vectors.
                alpha=alpha,#Learning rate will linearly drop to min_alpha over all inference epochs. 
                min_alpha=0.00025, # The initial learning rate
                min_count=1,#Ignores all words with total frequency lower than this
              dm =1) #1,0 – Defines the training algorithm. If dm=1, ‘distributed memory’ (PV-DM)
                                                          # If dm=0, 'distributed bag of words'(PV-DBOW) 


#Building a Vocabulary (a training corpus)
model.build_vocab([x for x in tagged_data])

model.train(utils.shuffle([x for x in tagged_data]), total_examples=len(tagged_data), epochs=max_epochs)

model.save('d2vec.model')
print(len(model.docvecs))
# def vec_for_learning(model, tagged_docs):
#     sents = tagged_docs
#     targets, regressors = zip(*[(doc.tags[0], model.infer_vector(doc.words, steps=20)) for doc in sents])
#     return targets, regressors

# y_train, X_train = vec_for_learning(model, tagged_data)
# y_test, X_test = vec_for_learning(model, tagged_data_test)

# import pickle

# #algo 1 (LOGISTIC REGRESSION)
# from sklearn.metrics import accuracy_score, f1_score
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# logreg = LogisticRegression(n_jobs=1, C=1e5)
# logreg.fit(X_train, y_train)
# pickle.dump(logreg, open('d2vlr_model.sav', 'wb'))
# y_pred = logreg.predict(X_test)

# print('Testing accuracy %s' % accuracy_score(y_test, y_pred))
# print('Testing F1 score : {}'.format(f1_score(y_test, y_pred, average='weighted')))

# #algo 2 (KNN)-optimized
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=10, weights='distance')
# knn.fit(X_train, y_train)
# predicted = knn.predict(X_test)
# pickle.dump(knn, open('d2vknn_model.sav', 'wb'))
# print(accuracy_score(y_test,predicted))

# #algo 3 (SVM)
# from sklearn.svm import LinearSVC
# svm = LinearSVC(class_weight='balanced', max_iter=3000, penalty='l1',dual=False)
# svm.fit(X_train, y_train)
# predicted = svm.predict(X_test)
# pickle.dump(svm, open('d2vsvm_model.sav', 'wb'))
# print(accuracy_score(y_test,predicted))

# #algo 4 (RF)
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification
# rfclf=RandomForestClassifier(random_state=52, bootstrap=False, max_features='auto', n_estimators=1000, class_weight='balanced')
# rfclf.fit(X_train, y_train)
# predicted=rfclf.predict(X_test)
# pickle.dump(rfclf, open('d2vrf_model.sav', 'wb'))
# print(accuracy_score(y_test, predicted))