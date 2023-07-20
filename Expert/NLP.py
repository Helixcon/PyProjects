import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

# Download stopwords and punkt tokenizer
nltk.download("stopwords")
nltk.download("punkt")

def text_summarization(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words
    words = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [[word for word in sentence if word not in stop_words] for sentence in words]

    # Calculate word frequency
    word_freq = FreqDist([word for sentence in words for word in sentence])

    # Calculate sentence scores based on word frequency
    sentence_scores = {sentence: sum(word_freq[word] for word in sentence) for sentence in words}

    # Sort sentences based on their scores in descending order
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    # Select the top N sentences for the summary
    top_sentences = [sentence for sentence, _ in sorted_sentences[:num_sentences]]

    # Join the top sentences to create the summary
    summary = " ".join(top_sentences)
    return summary

if __name__ == "__main__":
    # Sample text for summarization
    sample_text = """
    Natural language processing (NLP) is a subfield of artificial intelligence (AI)
    that focuses on the interaction between computers and humans through natural language.
    NLP techniques are used to enable computers to understand, interpret, and generate
    human language in a way that is both meaningful and useful.
    """

    # Perform text summarization
    summary = text_summarization(sample_text, num_sentences=2)
    print("Text Summary:")
    print(summary)

