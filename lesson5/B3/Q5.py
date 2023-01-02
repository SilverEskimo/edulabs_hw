# Write a Python function to check whether a string is a pangram or not.
# Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
from string import ascii_lowercase


def check_if_pangram(words: str) -> bool:
    words = words.lower()
    words = words.replace(" ", "")
    for char in ascii_lowercase:
        if char not in words:
            return False
    return True


example = "The quick brown fox jumps over the lazy dog"
print(check_if_pangram(example))