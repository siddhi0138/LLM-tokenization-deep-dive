import tiktoken

# Load GPT-style tokenizer
enc = tiktoken.get_encoding("cl100k_base")

words = [
    "unbelievable",
    "internationalization",
    "photosynthesis",
    "calculateTotalAmount",
    "HTTPRequestHandler"
]

print("=== TOKEN SPLITTING EXAMPLES ===\n")

for word in words:
    tokens = enc.encode(word)
    print(f"Input: {word}")
    print(f"Token count: {len(tokens)}")
    print(f"Tokens: {tokens}")
    print("-" * 40)
