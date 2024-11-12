import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load the pre-trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sentiment(review):
    # Transform the review into the same format as the training data
    review_vectorized = vectorizer.transform([review])
    prediction = model.predict(review_vectorized)
    
    return "Fake Review" if prediction[0] == 1 else "Genuine Review"
