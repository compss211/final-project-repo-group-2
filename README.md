# COMPSS-211-Final-Project-Template-Repo
Pei's Repository for COMPSS-211 Final Projects

## Contributor: Pei Zheng

# **NLP Topic Modeling Analysis**

This repository contains an end-to-end workflow for analyzing large-scale customer reviews using transformer-based topic modeling. The goal of this project is to identify dominant themes in customer discourse, quantify topic-level sentiment through average star ratings, and extract actionable business insights based on consumer feedback patterns.

---

## **Project Overview**

This project applies **BERTopic**—a transformer-embedding-based topic modeling framework—to uncover key themes embedded in millions of product reviews. Each review is cleaned, encoded into semantic embeddings, assigned to a topic cluster, and evaluated through topic-level average ratings to distinguish highly positive and negative customer experiences.

---

## **Methods Summary**

### **1. Data Cleaning & Preparation**

* Removed null texts and filtered out reviews with ≤10 words.
* Performed light text normalization (lowercasing, punctuation removal).
* Extracted clean review corpus for modeling.

### **2. Topic Modeling with BERTopic**

* Generated semantic embeddings using the **all-MiniLM-L6-v2** transformer.
* Dimensionality reduction + density-based clustering.
* BERTopic extracted:

  * Topic keywords
  * Topic frequencies
  * Topic assignments for each review

### **3. Visualization**

* Topic frequency bar charts
* Rating distribution comparisons

---

## **Key Findings**

* **Positive topics** are driven by emotional value, gift-giving contexts, perceived quality, and good deals.
* **Negative topics** center around waste of money, poor material quality, and incorrect sizing.
* Consumer satisfaction is highly influenced by **trust, expectation alignment, and emotional resonance**, not just product functionality.

---

## **Business Insights**

* Highlight gift-related messaging in marketing campaigns.
* Strengthen product description accuracy to reduce expectation gaps.
* Improve quality control for frequently criticized attributes (durability, materials, sizing).
* Use topic monitoring to detect early warning signals of emerging issues.

---

## **Dependencies**

Core libraries used in the project:

```txt
bertopic
pandas
numpy
scikit-learn
sentence-transformers
matplotlib
```
