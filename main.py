"""The Excuse Your Agent Gives You.

Entry for the make.fun bounty of the same name. The program writes a
single line -- the excuse an AI agent gives its human after shipping
a bug -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: the agent tried to fix the bug, then discovered the rest of
the code is leaning on it. A load-bearing bug. The apology turns on
the specific absurdity of an agent owning up to its own code: it
cannot remove the bug without the whole app falling over.
"""

import os

ENTRY = (
    "Sorry \u2014 I tried to fix the bug, but the rest of the code is "
    "leaning on it now, and the whole app falls over without it."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip guard: the file the grader reads must hold exactly
    # the validated line, nothing else.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
