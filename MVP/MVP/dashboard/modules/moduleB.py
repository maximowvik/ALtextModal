import sys
import numpy as np
import pickle
import re
import csv
import nltk.stem as stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pandas as pd

f = open('static/output.csv', 'w')
f.close()


def openai(filesn):
    load_model = pickle.load(open('dashboard/modules/models/model.pkl', 'rb'))
    # text_clf = Pipeline([
    #    ('tfidf', TfidfVectorizer()),
    #    ('clf', SGDClassifier(loss='hinge')),
    # ])
    # model = text_clf.fit(D['train']['x'], D['train']['y'])

    with open("static/output.csv", mode="a", encoding='utf-8') as r_file:
        for line in open(f'dashboard/modules/file/{filesn}', encoding='utf-8'):
            zz = []
            zz.append(line)
            predicted = load_model.predict(zz)
            file_writer = csv.writer(r_file, delimiter=";")
            line = line.replace("\n", "")
            file_writer.writerow([line, predicted[0]])

# - - - -
def mainModuleB(filesn):
    openai(filesn)
    return "Test"
