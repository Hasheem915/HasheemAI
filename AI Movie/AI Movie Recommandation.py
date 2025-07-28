import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Corrected function
def load_data(file_path=r"C:\Users\farya\OneDrive\Desktop\AI Codigal\AI Movie\imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df["Genre"].fillna(" ") + " " + df["Overview"].fillna("")
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        sys.exit()

# Load data
movies_df = load_data()

# TF-IDF and similarity
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies_df["combined_features"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


