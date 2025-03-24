import re
import nltk
import spacy
from keybert import KeyBERT

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

def extract_topics(text, num_topics=3):
    if not text or len(text) < 20:
        return ["General News"]

    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
    topics = [kw[0] for kw in keywords[:num_topics]]

    return topics
