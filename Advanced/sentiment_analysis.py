import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords, movie reviews, and punkt tokenizer
nltk.download("stopwords")
nltk.download("punkt")



# Load the movie review dataset
data = pd.read_csv("movie_reviews.csv")

# Preprocessing
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

data["review"] = data["review"].apply(preprocess_text)

# Create feature vectors using CountVectorizer
vectorizer = CountVectorizer(max_features=5000)
X = vectorizer.fit_transform(data["review"]).toarray()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, data["sentiment"], test_size=0.2, random_state=42)

# Train the classifier (Naive Bayes)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
