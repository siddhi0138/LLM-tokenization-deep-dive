import tiktoken

# Load GPT-style tokenizer
enc = tiktoken.get_encoding("cl100k_base")

sentences = {
    "English": "I am learning artificial intelligence",
    "Hindi": "मैं कृत्रिम बुद्धिमत्ता सीख रहा हूँ",
    "French": "J'apprends l'intelligence artificielle",
    "Spanish": "Estoy aprendiendo inteligencia artificial",
    "Japanese": "私は人工知能を学んでいます"
}

print("=== MULTILINGUAL TOKENIZATION COMPARISON ===\n")

for language, text in sentences.items():
    tokens = enc.encode(text)
    print(f"Language: {language}")
    print(f"Text: {text}")
    print(f"Token count: {len(tokens)}")
    print("-" * 50)
