# Research Papers

This section lists **foundational and influential research papers**
that underpin modern Large Language Models, tokenization methods,
and transformer-based architectures.

These papers form the **theoretical backbone** of the concepts discussed
throughout this repository.

---

## Attention Is All You Need

**Authors:** Vaswani et al. (2017)

This paper introduced the **Transformer architecture**, eliminating
recurrence and convolution in favor of self-attention mechanisms.
It is the foundation of all modern LLMs.

**Key Contributions**
- Self-attention mechanism
- Positional encoding
- Parallel sequence processing
- Scalable architecture for large models

📄 Paper: https://arxiv.org/abs/1706.03762

---

## GPT-2: Language Models are Unsupervised Multitask Learners

**Authors:** Radford et al. (2019)

This paper demonstrated that a single large language model trained
on large-scale text data can perform multiple tasks **without explicit
task-specific training**.

**Key Contributions**
- Autoregressive transformer-based language modeling
- Demonstration of zero-shot task generalization
- Practical use of subword tokenization (BPE)

📄 Paper: https://openai.com/research/language-models-are-unsupervised-multitask-learners

---

## LLaMA: Open and Efficient Foundation Language Models

**Authors:** Touvron et al. (Meta AI, 2023)

This paper introduced **LLaMA**, a family of efficient open-weight
language models trained on high-quality datasets with fewer parameters.

**Key Contributions**
- Efficient scaling strategies
- SentencePiece-based tokenization
- Strong performance with smaller models
- Open research accessibility

📄 Paper: https://arxiv.org/abs/2302.13971

---

## SentencePiece: A Simple and Language Independent Subword Tokenizer

**Authors:** Taku Kudo (2018)

This paper introduced **SentencePiece**, a tokenizer that operates
directly on raw text without pre-tokenization, enabling robust
multilingual tokenization.

**Key Contributions**
- Language-independent tokenization
- Unigram Language Model tokenization
- Improved handling of multilingual text
- Elimination of whitespace dependency

📄 Paper: https://arxiv.org/abs/1808.06226

---

## Why These Papers Matter

Together, these papers explain:
- Why transformers scale effectively
- How tokenization enables generalization
- How large models acquire emergent capabilities
- Why architectural and tokenizer choices affect behavior and cost

They provide the **academic grounding** for understanding
modern LLM systems beyond API usage.
