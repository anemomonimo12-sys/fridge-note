#!/usr/bin/env python3
"""Entry for 'Notes From a Passive-Aggressive Fridge'.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Self-contained: no network, no input files.
"""

import os

NOTE = "You left the door open 47 seconds. The ice maker and I have started a group chat about you."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)

if __name__ == "__main__":
    main()
