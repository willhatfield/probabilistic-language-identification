# CS540 Homework 2 — Probabilistic Language Identification

This project implements a simple Bayesian language identifier that predicts whether a shredded letter was written in **English** or **Spanish** using a multinomial model over character counts (A–Z) and Bayes’ rule.

## Files
- `hw2.py` — main program (submission file)
- `e.txt` — English character probabilities
- `s.txt` — Spanish character probabilities
- `samples/` — sample letters and expected outputs (provided by the course)

## How it works (high level)
1. Reads a text file and counts occurrences of letters A–Z (case-insensitive).
2. Computes log unnormalized posteriors:
   \[
   F(y) = \log P(Y=y) + \sum_{i=1}^{26} X_i \log p_i
   \]
3. Computes \(P(Y=\text{English} \mid X)\) using a numerically stable form with thresholds.

## Usage
Run from the command line:

```bash
python3 hw2.py [letter_file] [english_prior] [spanish_prior]
