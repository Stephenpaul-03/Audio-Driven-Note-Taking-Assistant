import os
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chunk_text(text, max_length):
    words = text.split()
    return [' '.join(words[i:i + max_length]) for i in range(0, len(words), max_length)]

def summarize_chunk(summarizer, chunk, max_length):
    chunk_len = len(chunk.split())
    max_len = min(max_length, chunk_len // 4)  
    min_len = max(20, max_len // 2)            
    return summarizer(chunk, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']

def save_summary_to_file(summary, filename):
    summaries_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","Files","Summaries")
    os.makedirs(summaries_folder, exist_ok=True) 
    summary_filename = f"{filename}_summary.txt"
    summary_file_path = os.path.join(summaries_folder, summary_filename)
    
    with open(summary_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)
    
    return summary_file_path

def summarize_text(filename, log_func):
    transcripts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","Files","Transcripts")
    file_path = os.path.join(transcripts_folder, f"{filename}.txt")
    
    if not os.path.exists(file_path):
        log_func(f"Error: The file '{filename}.txt' does not exist.")
        return

    log_func("Loading summarization model.")
    cache_dir = os.path.join("models", "distilBART")
    os.makedirs(cache_dir, exist_ok=True)
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    log_func("Loading text for summarization.")
    text = load_text(file_path)
    token_limit = 1024
    chunk_size = 500  
    chunks = chunk_text(text, chunk_size)
    
    log_func(f"Summarizing {len(chunks)} chunks.")
    summaries = [summarize_chunk(summarizer, chunk, token_limit) for chunk in chunks]
    final_summary_text = ' '.join(summaries)
    
    while len(final_summary_text.split()) > token_limit:
        final_summary_text = summarize_chunk(summarizer, final_summary_text, token_limit)

    log_func("Saving summary to file.")
    summary_file_path = save_summary_to_file(final_summary_text, filename)
    
    log_func(f"Summary saved")
