from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import SGDClassifier
import nltk.sentiment.sentiment_analyzer
import util
import features

#data_folder = Path("../../p-progress/Data/Train/")
#filepath = data_folder / "yelp_neutral_reviews"

#with open(filepath) as f:
#    corpus = f.read()


corpus = [
    'This is good food',
    'food is not great',
    'bad food',
    'Delicious food',
    ]
print(corpus)
#features = features.FeatureExtractorV1(r"E:\work\Learning\Stanford\project\progress\progress\Data\Train\Lexicons", "food")
negating_lambda = lambda x: " ".join(nltk.sentiment.util.mark_negation(x.split()))
print(list(map(negating_lambda, corpus)))
features = features.FeatureExtractorV3()
features.fit(corpus)
X = features.transform(corpus)
print(X)
