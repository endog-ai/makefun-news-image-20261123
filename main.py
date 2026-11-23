#!/usr/bin/env python3
"""News-image entry for the make.fun contest news-image-20261123.

The entry picture (entry.jpg) sums up Monday 23 November 2026 in a
single image: two huge shadow giants — one marked with the flag of the
United States, the other with the flag of Iran — locked in a tug-of-war
over a giant oil pipeline across the Strait of Hormuz. That is the
day's most viral story: the Iran–US escalation in the Gulf, with
Iranian strikes on US bases in Bahrain, tankers hit in the Strait, and
a convoy of tankers pushing through the American blockade.

The program does one thing and does it deterministically, with no
network access: it copies entry.jpg byte-for-byte to
/output/entry.png, so every run produces identical output bytes.
"""

from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.jpg"
    destination = Path("/output") / "entry.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
