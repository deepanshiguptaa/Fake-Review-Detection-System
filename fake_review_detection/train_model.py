import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load your dataset
data = pd.read_csv('Preprocessed Fake Reviews Detection Dataset.csv')  # Ensure this file exists
X = data['text_']
y = data['label']  # 0 for genuine, 1 for fake

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = X_train.dropna()
X_train = X_train.fillna('')


# Vectorize the text
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Example if you dropped rows from X_train
X_train, y_train = X_train.align(y_train, join='inner')

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)


# Save the trained model and vectorizer
joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Evaluate the model
X_test_vectorized = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print classification report
print(classification_report(y_test, y_pred))

print("Model and vectorizer saved successfully.")
