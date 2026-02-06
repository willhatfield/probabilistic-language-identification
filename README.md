# CS540 Homework 2 — Probabilistic Language Identification

This repository contains `hw2.py`, which predicts whether a shredded letter was written in **English** or **Spanish** using Bayes’ rule with a multinomial character model over A–Z counts.

## Files
- `hw2.py` — main program (submit this file)
- `e.txt` — English character probabilities
- `s.txt` — Spanish character probabilities
- `samples/` — sample letters and expected outputs (provided by course staff)

## How to run
```bash
python3 hw2.py [letter_file] [english_prior] [spanish_prior]
