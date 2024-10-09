import os
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def summarize_text(file_path):
    cache_dir = os.path.join("models", "distilBART")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    word_count = len(text.split())
    target_word_count = word_count // 4
    max_length = target_word_count
    min_length = target_word_count // 2  

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    print("\nSummary:")
    print(summary[0]['summary_text'])

if __name__ == "__main__":
    file_name = input("Enter the file name (including .txt extension): ")
    username = os.getlogin()
    file_path = os.path.join(f"C:/Users/{username}/Documents/Hermes Texts", file_name)
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_name}' does not exist in 'C:/Users/{username}/Documents/Hermes Texts'.")
    else:
        summarize_text(file_path)
