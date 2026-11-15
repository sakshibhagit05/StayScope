
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.feature_extraction.text import CountVectorizer

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_airbnb.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("========== STAYSCOPE TEXT MINING ==========")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Prepare listing names
titles = df["name"].fillna("").astype(str)

# Remove empty listing names
titles = titles[titles.str.strip() != ""]

# Extract individual words
word_vectorizer = CountVectorizer(
    stop_words="english",
    ngram_range=(1, 1),
    max_features=20
)

word_matrix = word_vectorizer.fit_transform(titles)

word_counts = word_matrix.sum(axis=0).A1
words = word_vectorizer.get_feature_names_out()

word_results = pd.DataFrame({
    "term": words,
    "frequency": word_counts
})

word_results = word_results.sort_values(
    by="frequency",
    ascending=False
)

print("\nTop 20 Frequently Used Words:")
print(word_results.to_string(index=False))

# Extract two-word phrases
bigram_vectorizer = CountVectorizer(
    stop_words="english",
    ngram_range=(2, 2),
    max_features=20
)

bigram_matrix = bigram_vectorizer.fit_transform(titles)

bigram_counts = bigram_matrix.sum(axis=0).A1
bigrams = bigram_vectorizer.get_feature_names_out()

bigram_results = pd.DataFrame({
    "term": bigrams,
    "frequency": bigram_counts
})

bigram_results = bigram_results.sort_values(
    by="frequency",
    ascending=False
)

print("\nTop 20 Frequently Used Two-Word Phrases:")
print(bigram_results.to_string(index=False))

# Save keyword results
word_results.to_csv(
    os.path.join(OUTPUT_DIR, "frequent_words.csv"),
    index=False
)

bigram_results.to_csv(
    os.path.join(OUTPUT_DIR, "frequent_bigrams.csv"),
    index=False
)

# Visualize frequent words
plt.figure(figsize=(12, 7))

sns.barplot(
    data=word_results,
    x="frequency",
    y="term"
)

plt.title("Top 20 Frequently Used Words in Airbnb Listing Titles")
plt.xlabel("Frequency")
plt.ylabel("Words")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "frequent_words.png")
)

plt.show()

print("\nText Mining Completed Successfully!")
print("\nGenerated files:")
print("frequent_words.csv")
print("frequent_bigrams.csv")
print("frequent_words.png")

print("\n========== END ==========")
