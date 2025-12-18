# 🔢 Tokens to Embeddings in Large Language Models

After tokenization, text exists only as a sequence of **integer token IDs**.
These integers are **purely symbolic** and cannot be processed meaningfully by a neural network.

To enable learning, LLMs convert token IDs into **dense numerical vectors called embeddings**.

> **Key idea:**
> Embeddings are the first point where language becomes geometry.

---

## 1️⃣ From Discrete Symbols to Continuous Space

Token IDs are categorical values:

```
"apple" → 3290
"banana" → 15496
```

The numerical value itself:

* Has no magnitude meaning
* Has no ordering semantics
* Does not encode similarity

A neural network cannot infer that *apple* and *banana* are related from their IDs alone.

Embeddings solve this by mapping each token into a **continuous vector space**.

---

## 2️⃣ Embedding Matrix: The Core Structure

Every LLM contains a **trainable embedding matrix**:

```
E ∈ ℝ^(V × D)
```

Where:

* `V` = vocabulary size
* `D` = embedding dimension

Each row:

```
E[i] = embedding of token i
```

This matrix is:

* Initialized randomly
* Learned during training
* Shared across all inputs

📌 **Memory perspective:**
The embedding matrix is often one of the largest parameter blocks in the model.

---

## 3️⃣ Embedding Lookup Is Not Computation

Unlike linear layers, embedding lookup is:

* A direct index operation
* No multiplication
* No activation function

### Example

```
Input Token IDs:
[15496, 995, 13]

Lookup:
[E[15496], E[995], E[13]]
```

Result:

```
Sequence of vectors ∈ ℝ^D
```

📌 This makes embedding layers computationally cheap but memory-intensive.

---

## 4️⃣ Static Nature of Token Embeddings

At this stage:

* Each token has **exactly one embedding**
* The embedding does **not change with context**

Example:

```
"bank" in:
- river bank
- financial bank
```

Both map to the **same embedding vector** initially.

👉 Contextual meaning is introduced **later** via self-attention.

---

## 5️⃣ How Embeddings Learn Meaning

Embeddings are trained via **gradient descent**, driven by the language modeling objective:

```
Predict next token
↓
Compute loss
↓
Backpropagate error
↓
Update embeddings
```

Tokens that:

* Appear in similar contexts
* Co-occur frequently
* Play similar syntactic roles

→ Move closer together in embedding space.

This is an **emergent property**, not a rule-based one.

---

## 6️⃣ Geometry of Embedding Space

Embedding spaces exhibit:

* Clustering
* Directional semantics
* Linear relationships

Classic intuition:

```
king − man + woman ≈ queen
```

While not always exact in LLMs, **semantic directions still exist**.

📌 LLMs reason over **vector geometry**, not symbolic logic.

---

## 7️⃣ Embedding Dimension and Model Capacity

Embedding dimension (`D`) determines:

* Representational richness
* Information density per token

### Typical Sizes

| Model       | Embedding Dim |
| ----------- | ------------- |
| BERT-base   | 768           |
| GPT-2       | 768           |
| GPT-3       | 12288         |
| LLaMA-2 13B | 5120          |

### Trade-offs

**Higher dimension**

* Captures subtle semantics
* Supports complex reasoning
* Increases memory + compute

**Lower dimension**

* Faster and cheaper
* Limited expressiveness

📌 Embedding size scales with model ambition.

---

## 8️⃣ Relationship Between Tokenization and Embeddings

Tokenization defines:

* What symbols exist
* How often embeddings are reused

Example:

```
"unbelievable"
→ ["un", "bel", "ievable"]
```

Each subword:

* Has its own embedding
* Learns reusable meaning fragments

This improves:

* Generalization
* Handling of rare words
* Multilingual overlap

---

## 9️⃣ Special Token Embeddings (Very Important)

Special tokens also have embeddings:

* `<BOS>`
* `<EOS>`
* `<PAD>`
* `<SYSTEM>`
* `<USER>`
* `<ASSISTANT>`

These embeddings encode:

* Structural information
* Role boundaries
* Instruction hierarchy

📌 Many prompt-engineering effects come from **special token embeddings**, not text itself.

---

## 🔟 Embedding Sharing (Weight Tying)

In many LLMs:

* Input embedding matrix
* Output projection matrix

are **shared (tied weights)**.

Benefits:

* Fewer parameters
* Better generalization
* Stronger input–output alignment

This means:

```
Same vector space is used to read and write language
```

---

## 1️⃣1️⃣ Embeddings Are Still Not “Understanding”

At this stage:

* No reasoning
* No context
* No grammar awareness

Embeddings provide:

* A numerical substrate
* A semantic coordinate system

True understanding emerges only after:

* Positional encoding
* Self-attention
* Multiple transformer layers

---

## 🧠 Why This Stage Is Foundational

Embeddings determine:

* What patterns the model can represent
* How efficiently it learns
* How much nuance it can encode
* How language is geometrically structured

> **Bad embeddings cannot be fixed by deeper layers.**

---

## 🔑 Key Takeaways

* Token IDs are meaningless without embeddings
* Embeddings map discrete symbols into continuous space
* They are learned, not designed
* Context is added later via attention
* Embeddings are the numerical foundation of all LLM intelligence

---

