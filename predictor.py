
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
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
            ret_dict[cat] = { 'category':cat_dict[cat][prediction.tolist().index(1)], 'index':prediction.tolist().index(1)+1 }
        else:
            ret_dict[cat] = { 'category':'none', 'index':0 }
    return ret_dict

# def train_classifiers(M,Y):
#     y_dict = {
#         'polarity': Y[:, :10],
#         'intensity': Y[:, 10:17],
#         'expression': Y[:, 17:22],
#         'attitude': Y[:, 22:37]
#     }
#
#     classifiers = {}
#
#     for cat, y in y_dict.items():
#         # remove data that doesn't provide any insight ( rows containing all 0s )
#         goodrows = np.where(y.sum(1)>0)[0]
#         y = y[goodrows, :]
#         m = M[goodrows, :]
#
#         m_ = TfidfTransformer(use_idf=True, sublinear_tf=True).fit_transform(m)
#
#         classifiers[cat] = RandomForestClassifier(n_estimators=25).fit(m_, y)
#
#     return classifiers

# if __name__ == '__main__':
#     cvect = CountVectorizer(ngram_range=(1,3), max_df=0.75)
#
#     M, Y, category_dictonary, cvect = make_m_y(cvect)
#     clfs = train_classifiers(M,Y)
#
#     for cat,clf in clfs.items():
#         dump(clf, 'classifiers/%s.pkl' % cat)
