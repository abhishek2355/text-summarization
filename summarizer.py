import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

# Download required data (first run only)
nltk.download('punkt_tab')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    # Split Paragraph into Sentences
    sentences = sent_tokenize(text)

    # Split Text into Words
    words = word_tokenize(text.lower())

    # Stop words = common words with low meaning (e.g is, the, and, from, it, in, of, etc.)
    stop_words = set(stopwords.words('english'))

    # Create Word Frequency Dictionary
    word_frequency = defaultdict(int)
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequency[word] += 1

    # Stores importance score of each sentence
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequency:
                sentence_scores[sentence] += word_frequency[word]

    # Pick Top Sentences
    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    # Combine Summary Sentences
    return " ".join(summary_sentences)
