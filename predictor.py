from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.joblib import dump,load
import numpy as np

def load_clfs():
    cvect = load('classifiers/cvect.pkl')

    cat_dict = {
        'polarity': ['positive', 'negative', 'both', 'neutral', 'uncertain-positive',
            'uncertain-negative', 'uncertain-both', 'uncertain-neutral', 'sentiment-positive',
            'sentiment-neg'],
        'intensity': ['low', 'low-medium', 'medium', 'medium-high', 'high', 'high-extreme',
            'extreme'],
        'expression': ['neutral', 'low', 'medium', 'high', 'extreme'],
        'attitude': ['positive', 'negative', 'sentiment-pos', 'sentiment-neg', 'arguing-pos',
            'arguing-neg', 'agree-pos', 'agree-neg', 'intention-pos', 'intention-neg',
            'speculation', 'other-attitude', 'both', 'interior-sentiment-pos', 'interior-sentiment-neg']
    }

    clfs = {}

    for k, _ in cat_dict.items():
        clfs[k] = load('classifiers/%s.pkl' % k)

    return [clfs, cvect, cat_dict]

def make_predict( clfs, cvect, cat_dict, text ):
    ret_dict = {}
    for cat,clf in clfs.items():
        prediction = np.squeeze(clf.predict(cvect.transform([text])))
        if 1 in prediction:
            ret_dict[cat] = { 'category':cat_dict[cat][prediction.tolist().index(1)] }
        else:
            ret_dict[cat] = { 'category':'none' }
    return ret_dict
