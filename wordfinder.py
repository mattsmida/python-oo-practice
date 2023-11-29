from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_given):
        """ Given a file path, read the file and create a list of words.
            and print the number of words. """
        self.read_file = open(file_given, "r", encoding = "utf-8")
        self.words = self.read_file.read().splitlines(False)
        self.read_file.close()
        print(self.describe())

    def random(self):
        """ Returns a random word from the list of words. """
        return choice(self.words)

    def describe(self):
        """ Returns the numbeself.read_file.splitlines()r of words in the file. """
        num_of_words = len(self.words)
        return f"{num_of_words} words read"


class RandomWordFinder(WordFinder):

    def __init__(self, file_given):
        """ Given a file path, read the file and create a list of words while
            excluding lines that are blank and with comments, then print
            the number of words. """
        super().__init__(file_given)
        self.words = [word for word in
                      self.words if word and word[0] != "#"]


