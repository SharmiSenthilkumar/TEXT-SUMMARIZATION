from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    max_chunk = 500
    text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    
    summary = ""
    for chunk in text_chunks:
        input_tokens = len(chunk.split())
        adjusted_max_length = min(130, max(30, int(input_tokens * 0.75)))
        result = summarizer(chunk, max_length=adjusted_max_length, min_length=20, do_sample=False)
        summary += result[0]['summary_text'] + "\n"

    
    return summary.strip()

if __name__ == "__main__":
    print("Enter your article text (end input with ENTER twice):")
    input_lines = []
    while True:
        line = input()
        if line == "":
            break
        input_lines.append(line)
    
    article_text = " ".join(input_lines)
    
    print("\n--- Original Text ---")
    print(article_text)
    
    print("\n--- Summary ---")
    print(summarize_text(article_text))
