from flask import Flask, jsonify, render_template
from predictor import make_predict, load_clfs
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.joblib import dump,load
import numpy as np
import urllib

app = Flask(__name__, static_url_path='')

@app.route('/predict/<text>')
def make_predicition(text):
    # return urllib.unquote(text).decode('utf8')
    return jsonify(make_predict(clfs,cvect,cat_dict,text))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    clfs, cvect, cat_dict = load_clfs()

    app.run()
