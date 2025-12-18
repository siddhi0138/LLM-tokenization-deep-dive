# Token Splitting Examples

Modern LLMs use **subword tokenization**, where words are broken into
smaller units called *subwords* instead of being treated as whole words.

This allows models to handle rare words, new words, and different word forms
without exploding vocabulary size.

---

## Why Token Splitting Happens

Tokenizers are designed to:
- Keep frequent words as single tokens
- Split rare or long words into smaller pieces
- Reuse common subword patterns across words

This improves generalization but increases token count.

---

## Common Token Splitting Patterns

### Long Words
```

unbelievable
→ ["un", "bel", "ievable"]

```

### Compound Words
```

internationalization
→ ["inter", "national", "ization"]

```

### Identifiers (from code)
```

calculateTotalAmount
→ ["calculate", "Total", "Amount"]

```

---

## Why This Matters for LLMs

Token splitting affects:
- Context window usage
- Cost (more tokens = higher cost)
- Reasoning stability for long words
- Handling of technical and domain-specific terms

Words that split into many tokens require the model to track
more elements simultaneously.

---

## Behavioral Impact

Heavily fragmented words:
- Increase attention load
- Are more prone to reasoning errors
- Can lead to inconsistent generation

This is especially important in:
- Scientific text
- Medical terminology
- Programming identifiers

---

## Runnable Demonstration

See `token_splitting.py` for a practical demonstration showing how
different words are split into multiple tokens using a GPT-style tokenizer.


Just say **“next”** when you’re ready.
