# Reading cleaned dataset
import pandas as pd
df = pd.read_csv('./cleaned_dataset.csv')

# Splitting the dataset into train and test sets
X = df.loc[:,'Judgement'].values
y = df.loc[:,'label'].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizinf the corpus using TFIDF Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
cv= CountVectorizer(ngram_range=(1,3), max_features=5000)
X_train_counts= cv.fit_transform(X_train)
tfidf_transformer = TfidfTransformer(use_idf=False)
train_vectors = tfidf_transformer.fit_transform(X_train_counts)
X_test_counts= cv.transform(X_test)
test_vectors = tfidf_transformer.transform(X_test_counts)

from  sklearn.metrics  import accuracy_score
from  sklearn.metrics  import recall_score
from  sklearn.metrics  import precision_score
from sklearn.metrics import confusion_matrix
# import scikitplot as skplt

#logistic regression as suggested by sklearn
#scaling inputvectors using maxabsscaler
from sklearn import preprocessing
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_mabs= max_abs_scaler.fit_transform(train_vectors)
X_test_mabs= max_abs_scaler.transform(test_vectors)

from sklearn.ensemble import RandomForestClassifier

rfclf=RandomForestClassifier(random_state= 4, bootstrap=False)
rfclf.fit(train_vectors, y_train)

predicted=rfclf.predict(test_vectors)
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))
# skplt.metrics.plot_confusion_matrix(y_test, predicted, figsize=(4,4))

#Logistic Regression with standardized values
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='liblinear', penalty='l1')
lr.fit(X_train_mabs, y_train)

predicted = lr.predict(X_test_mabs)
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))
# skplt.metrics.plot_confusion_matrix(y_test, predicted, figsize=(4,4))

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=2.2, fit_prior= False).fit(train_vectors, y_train)

predicted = clf.predict(test_vectors)
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))
# skplt.metrics.plot_confusion_matrix(y_test, predicted, figsize=(4,4))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=15, weights='distance')
knn.fit(X_train_mabs, y_train)

predicted = knn.predict(X_test_mabs)
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))
# skplt.metrics.plot_confusion_matrix(y_test, predicted, figsize=(4,4))

from sklearn.svm import LinearSVC
svm = LinearSVC(penalty='l1', dual=False, max_iter=1000, C=.5)
svm.fit(X_train_mabs, y_train)

predicted = svm.predict(X_test_mabs)
print('Accuracy Score = ',accuracy_score(y_test,predicted))
print('Recall Score = ',recall_score(y_test,predicted))
print('Precision Score = ',precision_score(y_test,predicted))
# skplt.metrics.plot_confusion_matrix(y_test, predicted, figsize=(4,4))

import pickle

pickle.dump(rfclf, open('BOWRF_model.sav', 'wb'))
pickle.dump(lr, open('BOWLR_model.sav', 'wb'))
pickle.dump(svm, open('BOWSVM_model.sav', 'wb'))
pickle.dump(knn, open('BOWKNN_model.sav', 'wb'))
pickle.dump(clf, open('BOWNB_model.sav', 'wb'))


