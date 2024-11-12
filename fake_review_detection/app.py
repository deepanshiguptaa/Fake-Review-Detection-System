from flask import Flask, request, render_template
import joblib

# Load the pre-trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    if not review:
        return render_template('index.html', prediction="Please enter a review.", review=review)
    
    sentiment = predict_sentiment(review)
    return render_template('index.html', prediction=sentiment, review=review)

def predict_sentiment(review):
    # Transform the review into the same format as the training data
    review_vectorized = vectorizer.transform([review])
    prediction = model.predict(review_vectorized)
    
    return "Fake Review" if prediction[0] == 1 else "Genuine Review"

if __name__ == '__main__':
    app.run(debug=True)
