import pandas as pd
#path = '/content/drive/My Drive/BE PROJECT/Lawgical Final/LabelledDataset/'
traindf = pd.read_csv('./train.csv')
testdf = pd.read_csv('./test.csv')
X_train = traindf.loc[:,'Judgement'].values
y_train = traindf.loc[:,'label'].values
X_test = testdf.loc[:,'Judgement'].values
y_test = testdf.loc[:,'label'].values

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from  sklearn.metrics  import accuracy_score
from  sklearn.metrics  import recall_score
from  sklearn.metrics  import precision_score
from sklearn.metrics import confusion_matrix

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=10000)
# vectorizer = pickle.load()
train_vectors = vectorizer.fit_transform(X_train)

import pickle
pickle.dump(vectorizer, open('TFIDFvectorizer.pickle', 'wb'))
test_vectors = vectorizer.transform(X_test)
#print(train_vectors.shape, test_vectors.shape)

from sklearn.feature_selection import RFE
#scaling inputvectors using maxabsscaler
from sklearn import preprocessing
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_mabs= max_abs_scaler.fit_transform(train_vectors)
X_test_mabs= max_abs_scaler.transform(test_vectors)

from  sklearn.metrics  import accuracy_score
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB(alpha=.0001).fit(train_vectors, y_train)
predicted=clf.predict(test_vectors)
# predicted = clf.predict(test_vectors)
print(accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))

from sklearn.naive_bayes import ComplementNB
cnb = ComplementNB(alpha=2, class_prior=[88,16]).fit(train_vectors, y_train)
from  sklearn.metrics  import accuracy_score
predicted = cnb.predict(test_vectors)
# print(accuracy_score(y_test,predicted))


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=30, weights='distance')
knn.fit(train_vectors, y_train)
print('KNN')
predicted = knn.predict(test_vectors)
print(accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))

from sklearn.svm import LinearSVC
from  sklearn.metrics  import accuracy_score
svm = LinearSVC(C=3, max_iter=5000)
svm.fit(X_train_mabs, y_train)
predicted = svm.predict(X_test_mabs)
print('SVM')
print(accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='liblinear', penalty='l1')
lr.fit(X_train_mabs, y_train)
predicted = lr.predict(X_test_mabs)
print('Logistic Regression')
print(accuracy_score(y_test, predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))

from sklearn.ensemble import RandomForestClassifier
rfclf=RandomForestClassifier(random_state=52, bootstrap=False, max_features='auto', n_estimators=1000, class_weight='balanced')
rfclf.fit(train_vectors, y_train)
predicted=rfclf.predict(test_vectors)
print('RandomForest')
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))


import pickle
svmfilename = 'svm_model.sav'
pickle.dump(svm, open(svmfilename, 'wb'))

nbfilename = 'nb_model.sav'
pickle.dump(clf, open(nbfilename, 'wb'))

knnfilename = 'knn_model.sav'
pickle.dump(knn , open(knnfilename, 'wb'))

lrfilename = 'lr_model.sav'
pickle.dump(lr, open(lrfilename, 'wb'))

rffilename = 'rf_model.sav'
pickle.dump(rfclf, open(rffilename, 'wb'))

