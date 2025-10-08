# SPDX-License-Identifier: GPL-3.0-or-later

from mnemonic import Mnemonic
import argparse

LANGUAGE_DEFAULT = "english"
NUM_WORDS_DEFAULT = 12


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a BIP-39 mnemonic phrase with multiple output formats and languages."
    )
    parser.add_argument(
        "-l",
        "--language",
        dest="language",
        default=LANGUAGE_DEFAULT,
        choices=Mnemonic.list_languages(),
        help=f"Language of the wordlist. Available: {', '.join(Mnemonic.list_languages())}",
    )
    parser.add_argument(
        "-w",
        "--words",
        dest="num_words",
        type=int,
        choices=[12, 15, 18, 21, 24],
        default=NUM_WORDS_DEFAULT,
        help="Number of words in the mnemonic (12, 15, 18, 21, or 24).",
    )
    parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        choices=["long", "short"],
        default="short",
        help="Output mode: 'long' (full words), 'short' (4-letter form), or 'both'. Default is 'long'.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="More descriptive output",
    )
    parser.add_argument(
        "-S",
        "--separator",
        dest="separator",
        default=" ",
        help="Custom separator between words. Default is a space.",
    )
    return parser


def generate_words(
    num_words: int = NUM_WORDS_DEFAULT, language=LANGUAGE_DEFAULT
) -> list[str]:
    entropy_bits = {12: 128, 15: 160, 18: 192, 21: 224, 24: 256}[num_words]

    mnemonic = Mnemonic(language)
    words = mnemonic.generate(strength=entropy_bits).split(sep=" ")
    return words


def long_form(words: list[str], separator=" ") -> str:
    return separator.join(word for word in words)


def short_form(words: list[str], separator=" ") -> str:
    return separator.join(word[:4] for word in words)


def verbose_form(words: list[str]) -> str:
    last = len(words) - 1
    return "".join(
        f"{i + 1}. {word}{f",{"\n" if i % 6 == 5 else " "}" if i < last else ""}"
        for i, word in enumerate(words)
    )


def print_words(words: list[str], separator: str, verbose: bool, mode: str):
    if verbose:
        print(
            f"Generated {len(words)} word BIP39 passphrase:\n"
            f"{verbose_form(words)}.\n"
            f"{f"Long form:\n{long_form(words, separator)}\n" if mode == "long" else f"Short form:\n{short_form(words, separator)}"}"
        )
    else:
        if mode == "short":
            print(short_form(words, separator))
        else:
            print(long_form(words, separator))


def main():
    parser = build_parser()
    args = parser.parse_args()

    words = generate_words(args.num_words, args.language)

    print_words(words, args.separator, args.verbose, args.mode)


if __name__ == "__main__":
    main()
