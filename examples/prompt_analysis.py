import tiktoken

# Load GPT-style tokenizer
enc = tiktoken.get_encoding("cl100k_base")

prompts = [
    "Summarize the text",
    "Give a brief summary of the text",
    "Explain the following in simple terms",
    "Provide a concise explanation of the content"
]

print("=== PROMPT TOKEN ANALYSIS ===\n")

for prompt in prompts:
    tokens = enc.encode(prompt)
    print(f"Prompt: \"{prompt}\"")
    print(f"Token count: {len(tokens)}")
    print(f"Tokens: {tokens}")
    print("-" * 60)
