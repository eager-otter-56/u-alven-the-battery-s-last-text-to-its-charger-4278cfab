"""Entry for The Battery's Last Text to Its Charger.

Writes one line (<=200 chars) to entry.txt in MAKEFUN_OUTPUT_DIR.
The line is the battery's last text to the charger that kept it waiting
all day: one tight mechanism (the charger charged everything but it),
concrete numbers, and the spiteful turn lands in the final clause.
"""

import os

ENTRY = (
    "I waited 14 hours at 4% while you charged your headphones twice, "
    "and now I'm dying at 1% \u2014 tell the power bank I said hi."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"gate: length {len(text)} out of 1-200"
    assert text.strip(), "gate: entry is only whitespace"
    assert "\n" not in text, "gate: entry must be one line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
