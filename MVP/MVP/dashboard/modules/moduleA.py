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


# очистка текста с помощью regexp приведение слов в инфинитив и нижний регистр, замена цифр

def text_cleaner(text):
    text = text.lower()  # приведение в нижний регистр
    stemmer = nltk.stem('russian')  # установка рускаого языка
    text = ' '.join(stemmer.stemWords(text.split()))
    text = re.sub(r'\b\d+\b', ' digit ', text)  # замена цифр
    return text


# загрузка данных из файла train_dataset_train.csv

def load_data(filesn):
    data = {'text': [], 'tag': []}
    with open(f"dashboard/modules/file/{filesn}", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        # Считывание данных из CSV файла
        for row in file_reader:
            data['text'] += [row[2]]
            data['tag'] += [row[1]]

    return data


# Обучение

def train_test_split(data, validation_split=0.1):
    sz = len(data['text'])
    print(sz)
    indices = np.arange(sz)
    np.random.shuffle(indices)

    X = [data['text'][i] for i in indices]
    Y = [data['tag'][i] for i in indices]
    nb_validation_samples = int(validation_split * sz)

    return {
        'train': {'x': X[:-nb_validation_samples], 'y': Y[:-nb_validation_samples]},
        'test': {'x': X[-nb_validation_samples:], 'y': Y[-nb_validation_samples:]}
    }


# - - - -


def openai(filesn):
    data = load_data(filesn)
    D = train_test_split(data)
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SGDClassifier(loss='hinge')),
    ])
    model = text_clf.fit(D['train']['x'], D['train']['y'])
    pickle.dump(model, open("dashboard/modules/models/model.pkl", 'wb'))
    pickle.dump(model, open("dashboard/modules/models/model.sav", 'wb'))
    predicted = text_clf.predict(D['train']['x'])


# - - - -
def mainModuleA(filesn):
    openai(filesn)
