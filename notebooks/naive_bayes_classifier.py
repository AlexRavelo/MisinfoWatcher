import spacy
import csv
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

dataset = pd.read_csv("datasets/Misinformation_Data_v2.csv")
count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()
dataset = dataset.fillna(' ')

# Splitting the data set into x and y, and making the dataset from that
x_train, x_test, y_train, y_test = train_test_split(dataset.title.to_numpy(), dataset.label.to_numpy(), random_state = 42)

x_train_dtm = count_vect.fit_transform(x_train)
x_train_vectorized = tfidf_transformer.fit_transform(x_train_dtm)
x_test_dtm = count_vect.transform(x_test)


naive_bayes = MultinomialNB()

naive_bayes.fit(x_train_vectorized, np.array(y_train))

y_pred = naive_bayes.predict(x_test_dtm)

print(metrics.classification_report(y_test, y_pred))
