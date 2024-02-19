import glob
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import sys
import ssl
import ssl


if len(sys.argv) != 4:
    print(sys.argv)
    print("Usage: python getstats.py <lyrics_language> '<absolute_lyrics_file_path/*.txt>' <lyrics_num_common>")
    sys.exit(1)

lyrics_language = sys.argv[1]
absolute_lyrics_file_path = sys.argv[2]
lyrics_num_common = int(sys.argv[3])

file_path_pattern = absolute_lyrics_file_path
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')  
os.makedirs(nltk_data_path, exist_ok=True) 
nltk.data.path.append(nltk_data_path)


def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Téléchargement des données nécessaires de NLTK...")
        _create_unverified_https_context = ssl._create_unverified_context
        ssl._create_default_https_context = _create_unverified_https_context
        nltk.download('punkt', download_dir=nltk_data_path, quiet=False)
        nltk.download('stopwords', download_dir=nltk_data_path, quiet=False)
        print("Données téléchargées.")

download_nltk_data()

def read_files(file_path_pattern):
    """Read and return the content of all files matching the file path pattern."""
    file_contents = []
    for filename in glob.glob(file_path_pattern):
        with open(filename, 'r', encoding='utf-8') as file:
            file_contents.append(file.read())
    return file_contents

def preprocess_and_tokenize(text, language=lyrics_language):
    """Tokenize text and remove stopwords and punctuation."""
    stop_words = set(stopwords.words(language))
    words = word_tokenize(text.lower(), language=language)  
    words = [word for word in words if word.isalpha() and word not in stop_words] 
    return words

def word_frequency_analysis(texts):
    """Perform word frequency analysis on a list of texts."""
    all_words = []
    for text in texts:
        all_words.extend(preprocess_and_tokenize(text))
    word_counts = Counter(all_words)
    return word_counts

def additional_analyses(word_counts):
    """Perform additional analyses: unique word count and average word length."""
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)
    average_word_length = sum(len(word) * count for word, count in word_counts.items()) / total_words
    return unique_words, average_word_length


lyrics = read_files(file_path_pattern)

word_counts = word_frequency_analysis(lyrics)

unique_words, average_word_length = additional_analyses(word_counts)

print(f"Unique words: {unique_words}")
print(f"Average word length: {average_word_length:.2f}")
print("Most common words:")
for word, count in word_counts.most_common(lyrics_num_common):
    print(f"{word}: {count}")
