import os

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from numpy import ndarray

from src.exception import CustomException
from sklearn.base import BaseEstimator, TransformerMixin


class Stem(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        corpus = []
        ps = PorterStemmer()
        for i in range(0, len(X)):
            review = re.sub('[^a-zA-z]', ' ', X[i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
            corpus.append(review)
        return corpus

class ToArray(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def tramsform(self, X):
        return X.toarray()