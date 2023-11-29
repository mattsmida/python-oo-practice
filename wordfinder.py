from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_given):
        """ Given a file path, get a list of words and print the number
        of words. """

        self.words = self.process_file(file_given)
        print(self.describe())

    def process_file(self, file_given):
        """Read the file given and create a list of words. Returns words list
        and close file"""

        read_file = open(file_given, "r", encoding="utf-8")
        words = read_file.read().splitlines(False)
        read_file.close()
        return words

    def random(self):
        """ Returns a random word from the list of words. """
        return choice(self.words)

    def describe(self):
        """ Returns the number of words in the file. """
        num_of_words = len(self.words)
        return f"{num_of_words} words read"



class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a special file."""

    def __init__(self, file_given):
        """ Given a file path, read the file and create a list of words while
            excluding lines that are blank and with comments, then print
            the number of words. """
    #we are changing the words in the child class, look up in the parent class and

        super().__init__(file_given)
        self.words = self.process_file()
        # def process_file:
    def process_file(self):
        super().process_file()
        words = [word for word in
                self.words if word and word[0] != "#"]
        print("word list:", words)
        return words
