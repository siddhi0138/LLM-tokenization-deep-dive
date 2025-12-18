# Prompt Token Analysis

Large Language Models are highly sensitive to **how prompts are phrased**.
Two prompts that look similar to humans can tokenize very differently.

This sensitivity arises because LLMs operate on **token sequences**, not on
semantic intent directly.

---

## Why Prompt Wording Matters

Tokenizers split text based on:
- Subword frequency
- Whitespace
- Punctuation
- Common phrase patterns

As a result, different phrasings of the same instruction may produce
different token boundaries and token counts.

---

## Example Prompts

```

"Summarize the text"

```
```

"Give a brief summary of the text"

```

Although both prompts request the same action, they produce different
token sequences internally.

---

## Impact on Model Behavior

Differences in tokenization can lead to:
- Different attention patterns
- Different probability distributions
- Variations in output style and detail
- Changes in cost and latency

This explains why **prompt engineering works** at a practical level.

---

## Token Count and Cost

Since LLM pricing is token-based:
- Verbose prompts cost more
- Inefficient phrasing wastes context
- Compact prompts improve performance and affordability

Prompt design is therefore a **token optimization problem**, not just
a linguistic one.

---

## Practical Guidance

When writing prompts:
- Prefer concise instructions
- Avoid unnecessary filler words
- Test multiple phrasings when precision matters

Small prompt changes can have disproportionately large effects.

---

## Runnable Demonstration

See `prompt_analysis.py` for a practical demonstration comparing
token counts across different prompt phrasings using a GPT-style tokenizer.
