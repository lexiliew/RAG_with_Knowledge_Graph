# IntelliGraph: Retrieval‑Augmented Generation with Knowledge Graphs (RAG\_KG)

> Capstone Project · Northeastern University Vancouver · Academic Year 2024‑2025

---

## ✨ Why IntelliGraph?

Large‑language models are brilliant storytellers—**and** serial exaggerators. They’ll hallucinate faster than you can say “citation needed.” **IntelliGraph** stitches a domain‑specific **Knowledge Graph (KG)** into the Retrieval‑Augmented Generation (RAG) loop, giving the model grounded facts, trimming hallucinations, and keeping your compliance team blissfully bored.

---

## 🔑 Key Contributions

| # | Contribution                                                                                            | Why You Care                                                         |
| - | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1 | **Graph‑Aware Retriever** combining semantic vector search (FAISS) *and* KG predicate/centrality scores | More relevant, context‑rich retrievals → better answers              |
| 2 | **Hybrid Memory Layer** orchestrated with LangChain, backed by Neo4j + FAISS                            | Scales to millions of docs without setting your GPU on fire          |
| 3 | **Metric Suite**: FactScore, BLEU, Hallucination Rate, and our very own **Graph Groundedness**          | Quantifies truthiness instead of guessing                            |
| 4 | **Comparative Study**: vanilla RAG vs RAG + KG across open‑domain QA & enterprise KM                    | Shows a **38 % drop** in hallucinations and **+7.4 BLEU** on average |

Under the hood this will:

1. **Ingest** → chunk docs + extract entities/relations → populate Neo4j & FAISS.
2. **Retrieve** top‑k passages **and** graph paths.
3. **Generate** an answer with the combined context.
4. **Evaluate** results & log metrics.

---

## 🧪 Experiments & Evaluation

* **Datasets**: UBC university policies.
* **Baselines**: GPT‑4o w/ semantic RAG; GPT‑4o + KG; vanilla GPT‑4o (zero‑shot).
* **Metrics**: factual consistency (FactScore), hallucination rate, BLEU, Graph Groundedness.

| Model                       | Hallucination ↓ | FactScore ↑ | BLEU ↑   |
| --------------------------- | --------------- | ----------- | -------- |
| GPT‑4o                      | 29 %            | 0.71        | 27.3     |
| **RAG**                     | 14 %            | 0.81        | 34.6     |
| **RAG + KG (IntelliGraph)** | **9 %**         | **0.87**    | **42.0** |
