import fasttext
import pandas as pd
#path = '/content/drive/My Drive/BE PROJECT/Lawgical Final/LabelledDataset/'
traindf = pd.read_csv('./train.csv')
testdf = pd.read_csv('./test.csv')

print(traindf.head())
from io import StringIO
col = ['label', 'Judgement']
cases = traindf[col]
print(cases.head())
cases['label']= ['__label__'+ str(s) for s in cases['label']]
print(cases)

import csv
cases.to_csv('train_cases.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
model = fasttext.train_supervised(input="train_cases.txt",lr=1.0,wordNgrams=3 ,epoch=25)
model.save_model("model_fasttext.bin")
X_test = testdf.loc[:,'Judgement'].values
y_test = testdf.loc[:,'label'].values
y_test= ['__label__'+ str(s) for s in y_test]

predicted=model.predict(X_test.tolist())
from sklearn.metrics import accuracy_score
print("Accuracy Score: ", accuracy_score(y_test,predicted[0]))
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
confusion_matrix(y_test, predicted[0])
print("Precision Score: ", precision_score(y_test,predicted[0], average='weighted'))
print("Recall Score: ", recall_score(y_test,predicted[0], average='weighted'))
