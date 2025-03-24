from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if not text or len(text) < 50:
        return text  # Return original if too short

    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]["summary_text"]
