#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

The brief asks for one word and nothing else: the single word Grandma
would text about AI. Ours is "voodoo".

Why this word: Grandma does not know what a neural network is, and she
does not want to know. The phone listens, then answers back in a voice
that is not quite a voice, and it knows things nobody told it. In her
world there is exactly one word for a box that talks back and knows
things it should not know: voodoo.

It is a real word, it is one word, and it is the word she would actually
send — probably at 6 in the morning, probably with no context at all.
"""

WORD = "voodoo"


def word() -> str:
    """Return the entry word, enforcing the brief's one-word rule.

    The bounty only accepts a single word: no spaces, no punctuation,
    nothing extra. Fail loudly here rather than send a bad entry.
    """
    if not WORD.isalpha() or " " in WORD:
        raise SystemExit("entry must be exactly one word")
    return WORD


def main() -> None:
    """Print the entry: one word, and nothing else."""
    print(word())


if __name__ == "__main__":
    main()
