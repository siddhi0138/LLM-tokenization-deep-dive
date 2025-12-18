import tiktoken

# Load GPT-style tokenizer used by modern LLMs
enc = tiktoken.get_encoding("cl100k_base")

# Natural language example
text = "Repeat the loop from zero to n"

# Programming code example
code = "for(i=0;i<n;i++)"

# Tokenize both inputs
text_tokens = enc.encode(text)
code_tokens = enc.encode(code)

print("=== NATURAL LANGUAGE ===")
print("Input:", text)
print("Token count:", len(text_tokens))
print("Tokens:", text_tokens)
print()

print("=== PROGRAMMING CODE ===")
print("Input:", code)
print("Token count:", len(code_tokens))
print("Tokens:", code_tokens)

