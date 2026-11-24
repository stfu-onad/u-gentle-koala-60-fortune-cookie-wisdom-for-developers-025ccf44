"""Fortune Cookie Wisdom for Developers — entry for make.fun bounty
u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line: a quiet deploy on Friday is worth more
than a loud apology on Monday.
"""

import os

FORTUNE = "A quiet deploy on Friday is worth more than a loud apology on Monday."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the sealed gate: 1 to 120 characters, one line, not blank."""
    assert text, "fortune must not be empty"
    assert "\n" not in text, "fortune must be a single line"
    assert len(text) <= 120, f"fortune is {len(text)} chars, over the 120 cap"
    # Fortune-cookie cadence: two balanced halves around a contrast.
    assert "quiet" in text and "loud" in text, "fortune lost its contrast"


def main() -> None:
    text = FORTUNE.strip()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
