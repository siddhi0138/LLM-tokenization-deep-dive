# 🧩 Token Types & Vocabulary in LLMs

Tokenization converts raw text into **tokens**, which are the smallest units a Large Language Model (LLM) can process.
These tokens are mapped to integers using a **fixed vocabulary**, forming the foundation of all downstream model behavior.

> **Key idea:**
> LLMs never see text. They only see **token IDs**.

---

## 1️⃣ What Is a Token?

A **token** is a discrete unit of text chosen by a tokenizer based on statistical patterns in training data.

Depending on the tokenizer design, a token may represent:

* A full word
* A part of a word (subword)
* A single character
* A raw byte
* A special control symbol

---

## 2️⃣ Types of Tokens

### 2.1 Word Tokens

**Definition:**
Each token corresponds to a complete word.

**Example:**

```
"I love NLP"
→ ["I", "love", "NLP"]
```

**Advantages**

* Easy to interpret
* Short token sequences

**Disadvantages**

* Very large vocabulary
* Cannot handle unseen words (OOV problem)
* Poor multilingual support

📌 **Result:**
❌ Not suitable for modern LLMs

---

### 2.2 Character Tokens

**Definition:**
Each character becomes a token.

**Example:**

```
"hello"
→ ["h", "e", "l", "l", "o"]
```

**Advantages**

* No unknown tokens
* Language independent

**Disadvantages**

* Extremely long sequences
* Weak semantic representation
* Slower training and inference

📌 **Result:**
Rarely used alone in LLMs

---

### 2.3 Subword Tokens (Most Important)

**Definition:**
Words are split into **frequently occurring word pieces**.

**Example:**

```
"unbelievable"
→ ["un", "bel", "ievable"]
```

This approach balances:

* Vocabulary size
* Semantic meaning
* Sequence length

**Why subwords work well**

* Common words stay whole
* Rare words are decomposed
* Shared morphemes improve generalization

📌 **Used by:** GPT, BERT, LLaMA, T5, Claude

---

### 2.4 Byte-Level Tokens

**Definition:**
Text is first converted into **raw bytes (0–255)**, then tokenized.

**Example:**

```
😀 → [240, 159, 152, 128]
```

**Advantages**

* No unknown tokens
* Handles emojis, symbols, code, and binary data
* Fully language-agnostic

**Disadvantages**

* Can increase token count for some text
* Less human-readable

📌 **Used by:** GPT-2+, GPT-3, GPT-4 (Byte-level BPE)

---

### 2.5 Special Tokens

**Definition:**
Non-text tokens that control model behavior.

| Token         | Purpose                  |
| ------------- | ------------------------ |
| `<BOS>`       | Beginning of sequence    |
| `<EOS>`       | End of sequence          |
| `<PAD>`       | Padding                  |
| `<UNK>`       | Unknown token            |
| `<MASK>`      | Masked prediction (BERT) |
| `<SYS>`       | System instruction       |
| `<USER>`      | User message             |
| `<ASSISTANT>` | Model response           |

These tokens **do not represent language**, but **structure and intent**.

---

## 3️⃣ Token Type Comparison Diagram

```
Raw Text
  |
  v
"I love tokenization!"

Word-level:
["I", "love", "tokenization!"]

Character-level:
["I"," ","l","o","v","e"," ","t","o","k","e","n","i","z","a","t","i","o","n","!"]

Subword-level:
["I"," love"," token","ization","!"]

Byte-level:
[73,32,108,111,118,101,32,116,111,107,101,110,105,122,97,116,105,111,110,33]
```

---

## 4️⃣ Vocabulary (Vocab)

### 4.1 What Is a Vocabulary?

A **vocabulary** is a fixed mapping:

```
Token → Integer ID
```

Example:

```
"token" → 15496
```

This mapping is learned during tokenizer training and **never changes** during inference.

---

### 4.2 Vocabulary Size in Real Models

| Model  | Vocabulary Size |
| ------ | --------------- |
| GPT-2  | ~50,257         |
| GPT-3  | ~50k            |
| LLaMA  | ~32k            |
| Claude | ~100k           |

---

## 5️⃣ Vocabulary Size Trade-offs

### Small Vocabulary

**Pros**

* Better generalization
* Faster softmax
* Lower memory usage

**Cons**

* More tokens per sentence
* Longer context usage
* Higher inference cost

---

### Large Vocabulary

**Pros**

* Shorter token sequences
* Better handling of rare words
* Fewer token splits

**Cons**

* Larger model size
* Slower training
* Higher memory consumption

---

### Vocabulary Trade-off Diagram

![Vocabulary Trade-off Diagram](../image1.png)

---

```
## 6️⃣ Token IDs vs Meaning (Critical Insight)

Tokens **have no meaning by themselves**.

```
Token ID: 15496
Meaning: None
```

Meaning emerges only after:

1. Embedding lookup
2. Contextual attention
3. Probability modeling

> **Tokens are indices, not ideas.**

---

## 7️⃣ Vocabulary Bias & Language Effects

Languages with:

* Rich morphology
* Long words
* Complex scripts

→ Tend to produce **more tokens**

This can lead to:

* Faster context exhaustion
* Higher cost
* Slight performance bias

📌 Example:

```
English sentence → 12 tokens
Same sentence in another language → 20+ tokens
```

---

## 8️⃣ Why Token Types & Vocabulary Matter

Token design affects:

* Model reasoning
* Multilingual performance
* Code understanding
* Cost efficiency
* Prompt sensitivity

> **Tokenization is not preprocessing — it is model architecture.**

---

## 9️⃣ Key Takeaways

* Tokens are the atomic units of LLMs
* Subword and byte-level tokens dominate modern models
* Vocabulary size is a critical trade-off
* Special tokens control structure and behavior
* All intelligence emerges from token prediction

---


