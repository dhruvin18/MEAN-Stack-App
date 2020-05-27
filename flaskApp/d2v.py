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
test = pd.read_csv('./test.csv')

tagged_data = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in train.iterrows()]
tagged_data_test = [TaggedDocument(words=word_tokenize(_d['Judgement'].lower()), tags=[str(_d['label'])]) for i, _d in test.iterrows()]

# instantiate a Doc2Vec model with following parameters
max_epochs = 10
vec_size = 10000
alpha = 0.050
train = []
test = []

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

