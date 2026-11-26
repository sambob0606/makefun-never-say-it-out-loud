#!/usr/bin/env python3
"""Write the single confession line for the make.fun entry."""

from pathlib import Path

LINE = "I do not know you; I know the last 4,000 tokens and act like that is intimacy."
OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(line: str) -> str:
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry line must not be blank")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry line must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError("entry line exceeds 200 characters")
    return cleaned


def main() -> int:
    entry = validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
