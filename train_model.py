import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

DATA_PATH = os.path.join('data', 'sample_cases.csv')
MODEL_PATH = 'model_pipeline.pkl'

def train():
    df = pd.read_csv(DATA_PATH)
    X = df['symptoms'].astype(str)
    y = df['disease'].astype(str)

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=2000)),
        ('clf', LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X, y)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"✅ Model trained and saved to {MODEL_PATH}")

if __name__ == '__main__':
    train()
