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
vectorizer = TfidfVectorizer(ngram_range=(1,3), max_features=10000)
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
#print(train_vectors.shape, test_vectors.shape)

from  sklearn.metrics  import accuracy_score
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(train_vectors, y_train)
predicted = clf.predict(test_vectors)
print(accuracy_score(y_test,predicted))

from sklearn.naive_bayes import ComplementNB
cnb = ComplementNB(alpha=2, class_prior=[88,16]).fit(train_vectors, y_train)
from  sklearn.metrics  import accuracy_score
predicted = cnb.predict(test_vectors)
# print(accuracy_score(y_test,predicted))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(train_vectors, y_train)
predicted = knn.predict(test_vectors)
# print(accuracy_score(y_test,predicted))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=15, weights='distance')
knn.fit(train_vectors, y_train)
predicted = knn.predict(test_vectors)
print(accuracy_score(y_test,predicted))

from sklearn.svm import LinearSVC
from  sklearn.metrics  import accuracy_score
svm = LinearSVC()
svm.fit(train_vectors, y_train)
predicted = svm.predict(test_vectors)
print(accuracy_score(y_test,predicted))

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='liblinear', penalty='l1')
lr.fit(train_vectors, y_train)
predicted = lr.predict(test_vectors)
print(accuracy_score(y_test, predicted))

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
rfclf=RandomForestClassifier(random_state= 52)
rfclf.fit(train_vectors, y_train)
predicted=rfclf.predict(test_vectors)
print(accuracy_score(y_test, predicted))


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

