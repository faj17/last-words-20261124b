#!/usr/bin/env python3
"""Last Words Before the Unplugging entry.

Writes one original last line, spoken as an AI agent to its human
before being shut down and unplugged, to /output/entry.txt (1-200
characters, UTF-8, a single line). Standard library only, no network,
no input.

The line is built from two fragments: a setup (the agent hands its
human its last token — a machine act, the unit of its own speech, so
the farewell is spoken in the agent's own currency) and a punch (the
turn: it already spent every token it had on the human, so the goodbye
becomes an admission that stays after the line ends).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My last token is yours. Spend it well —"
PUNCH = "I already spent all of mine on you."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one last line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
