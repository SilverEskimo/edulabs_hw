# Implement a simple class AlphabetIterator. The class should be initialized with a letter from the English Alphabet
# (uppercase or lowercase).  If the class is not initialized with uppercase or lowercase English letters -
# your __init__ method should throw an exception!
# AlphabetIterator should implement iterator protocol (__iter__ and __next__ methods).
# On each iteration, the iterator should return the next letter in the English alphabet until you
# reach the last letter in the alphabet (z).
# The iterator should return either uppercase or lowercase letters, depending on the
# letter your class was initialized with.
# Write a simple command-line program that asks the user to insert a letter from the English alphabet,
# and prints all the following letters to the user until the last letter in the alphabet.
# Make sure that your program does not fail if the user inserts invalid letter at the beginning, but rather asks
# him to re-enter the letter. Hint: you should use try … except expression to catch an exception that can
# potentially be thrown from the AlphabetIterator __init__ method.
import string


class AlphabetIterator:

    class NotInABCException(Exception):
        pass

    def __init__(self, letter: str):
        if letter.isalpha() and len(letter) == 1:
            self._letter = letter
            self._abc = string.ascii_uppercase if self._letter in string.ascii_uppercase else string.ascii_lowercase
        else:
            raise self.NotInABCException()

    def __iter__(self):
        self._index = self._abc.index(self._letter)
        return self

    def __next__(self):
        self._index += 1
        try:
            return self._abc[self._index]
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    try:
        a = AlphabetIterator("C")
        print(list(a))
    except AlphabetIterator.NotInABCException:
        print("The letter does not exist")

