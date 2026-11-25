#!/usr/bin/env python3
"""Variant B — SPEED angle for the Solana wallet agent slogan.

Concept: a swap that lands before the human finishes saying the word
"swap". One concrete scene (saying the word) + one surprising turn
(the trade is already settled before the sentence ends).

Version history (one concept, iterated):
  v1: Tell your Solana wallet agent to swap, blink, and it's already settled.
  v2: Say 'swap' to your Solana wallet agent — settled before the word leaves your mouth.
  v3: Your Solana wallet agent settles the swap before you finish saying the word 'swap'.
  v4: Blink: your swap is already settled. Your Solana wallet agent moves faster than your sentence.
  v5: Your swap settles before you finish saying 'swap' — your Solana wallet agent, already done.
  v6 (FINAL): Your swap is settled before you finish saying 'swap' — your Solana wallet agent, already done.
"""

import os

# v6 (FINAL) — "is settled" instead of "settles": the trade is already
# a done fact while the word is still being spoken. 14 words, ~100 chars.
SLOGAN = "Your swap is settled before you finish saying 'swap' \u2014 your Solana wallet agent, already done."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN)
    # Best-effort copy next to the repo root; the grader sandbox mounts
    # the repo read-only, so this must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(SLOGAN)
    except OSError:
        pass


if __name__ == "__main__":
    main()
