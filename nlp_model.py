import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("social_media_data.csv")

relatable_words = [
    "exactly","feel","felt","only","relatable","understood",
    "struggle","needed","brain","life","experience"
]

def make_label(text):
    text = str(text).lower()
    return "Relatable" if any(w in text for w in relatable_words) else "Neutral"

df["Sentiment_Label"] = df["Comment_Text"].apply(make_label)

X_train, X_test, y_train, y_test = train_test_split(
    df["Comment_Text"], df["Sentiment_Label"],
    test_size=0.25, random_state=42, stratify=df["Sentiment_Label"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))

joblib.dump(model, "relatability_model.joblib")

df["Predicted_Label"] = model.predict(df["Comment_Text"])
df.to_csv("sentiment_results.csv", index=False)

def predict_comment(comment):
    return model.predict([comment])[0]

if __name__ == "__main__":
    examples = [
        "I feel exactly like this every day.",
        "This is useful information."
    ]
    for e in examples:
        print(e, "=>", predict_comment(e))
