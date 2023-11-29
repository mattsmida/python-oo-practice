from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_given):
        """"""
        self.read_file = open(file_given, "r", encoding = "utf-8")
        self.words = self.read_file.read().splitlines(False)
        self.read_file.close()
        print(self.describe())

    def random(self):
        return choice(self.words)

    def describe(self):
        # print("words are:", self.words)
        num_of_words = len(self.words)
        #print("num of words:", num_of_words)
        return f"{num_of_words} words read"