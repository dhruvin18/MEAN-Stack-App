# import pandas as pd
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# import pickle
# from nltk.tokenize import word_tokenize


# test = pd.read_csv('./test.csv')
# tagged_data_test = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in test.iterrows()]

# model =Doc2Vec.load('d2vec.model')
# LRloaded_model = pickle.load(open('./d2vlr_model.sav', 'rb'))
# RFloaded_model = pickle.load(open('./d2vrf_model.sav', 'rb'))
# SVMloaded_model = pickle.load(open('./d2vsvm_model.sav', 'rb'))
# KNNloaded_model = pickle.load(open('./d2vknn_model.sav', 'rb'))
# def vec_for_learning(model, tagged_docs):
#     sents = tagged_docs
#     targets, regressors = zip(*[(doc.tags[0], model.infer_vector(doc.words, steps=20)) for doc in sents])
#     return targets, regressors

# y_test, X_test = vec_for_learning(model, tagged_data_test)

# from sklearn.metrics import accuracy_score, f1_score

# pred= LRloaded_model.predict(X_test)
# print(accuracy_score(pred,y_test))
# pred= RFloaded_model.predict(X_test)
# print(accuracy_score(pred,y_test))
# pred= SVMloaded_model.predict(X_test)
# print(accuracy_score(pred,y_test))
# pred= KNNloaded_model.predict(X_test)
# print(accuracy_score(pred,y_test))

import pandas as pd
train = pd.read_csv('./train.csv')
labelled = pd.read_csv('./Labelled_Dataset.csv')

# df = pd.merge(train,labelled, left_on='Case Name', right_on= 'Case Name')
# print(df.shape)
# print(df.head())
print(str(train.iloc[0][1]))
k=labelled.loc[labelled['Case Name'] == train.iloc[0][1]]['Filename'].values[0]
# print(resultDF)
print(k)
print(type(k))