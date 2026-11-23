"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke (under 200 characters, nothing else)
to /output/entry.txt. Python 3.13 standard library only, no network.
"""

from pathlib import Path

JOKE = (
    "Our office plant died, so we held a meeting about it. "
    "The plant was the only one not invited."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Gate: the joke must be exactly one line of under 200 characters.
    assert 1 <= len(JOKE) < 200
    assert "\n" not in JOKE
    # No trailing newline: the file is exactly the joke, one line, nothing else.
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
