#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single office joke, one line, to /output/entry.txt.
The line turns on a real office detail (the reply-all storm) and
lands its laugh in the last few words.
"""

LINE = "I replied-all to say please stop replying-all, and now there are forty-seven of us apologising in a thread."


def main():
    if not 1 <= len(LINE) <= 199:
        raise ValueError("entry must be 1-199 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
