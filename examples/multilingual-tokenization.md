# Multilingual Tokenization

Tokenization is **not equally efficient across languages**.
The same meaning expressed in different languages can result in
very different token counts.

This happens because most tokenizers are trained on data where
some languages are more dominant than others.

---

## Why Token Counts Differ Across Languages

Tokenizers are optimized to:
- Keep frequent subwords intact
- Split rare or less common character patterns

Languages with:
- Rich morphology
- Long compound words
- Non-Latin scripts

often produce **more tokens** for the same semantic content.

---

## Example Scenario

Meaning:
```

"I am learning artificial intelligence"

```

This sentence, when written in different languages, can expand into
very different numbers of tokens, even though the meaning is identical.

---

## Impact on LLM Performance

Higher token counts lead to:
- Faster context window exhaustion
- Higher inference cost
- Slight degradation in long-form reasoning
- Increased likelihood of truncation

This creates a **structural multilingual bias** in LLMs.

---

## Multilingual Generalization

Subword tokenization enables some cross-lingual transfer by sharing
common subword patterns.

However, languages with fewer shared subwords:
- Benefit less from pretraining
- Require more tokens
- Are less efficient in long prompts

---

## Practical Implications

When working with multilingual prompts:
- Be aware of token usage differences
- Avoid unnecessarily verbose phrasing
- Consider summarization for long inputs

Token efficiency is especially important in multilingual systems.

---

## Runnable Demonstration

See `multilingual.py` for a practical demonstration comparing
token counts across multiple languages using a GPT-style tokenizer.

