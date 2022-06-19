import random
import json

class FiveLetters:

    replace_e = True
    if replace_e:
        all_words = json.loads(open('dictionary.json', 'r').read().replace('ё', 'е'))
    else:
        all_words = json.loads(open('dictionary.json', 'r').read())

    def __init__(self, word_length=5):
        self.word_length = word_length

        self.__setup()

    def reset(self):
        self.__setup()

    def __setup(self):
        self.words = []
        for word in self.all_words:
            if len(word) == self.word_length: self.words.append(word)
        self.words_count = len(self.words)

        self.excluded_words = []

        self.excluded_letters = set()
        self.possible_letters = set()
        self.wrong_places = [set() for _ in range(self.word_length)]
        self.placed_letters = [None for _ in range(self.word_length)]

    def findBestWords(self):
        sorted_words = [[] for _ in range(0, self.word_length)]
        for word in self.words:
            sorted_words[len(set(word))].append(word)
        for proposed_words in sorted_words:
            if len(proposed_words) != 0:
                return proposed_words
        return []

    def nextWord(self):
        if len(self.words) == 0:
            return None
        return random.choice(self.words)

    def removeWord(self, word):
        self.words.remove(word)
        self.words_count = len(self.words)

    def setInfo(self, word, pattern):
        if pattern != '+' * self.word_length:
            self.excluded_words.append(word)

        for letter, letter_state, letter_number in zip(word, pattern, range(self.word_length)):
            if letter_state == '-' and letter not in self.possible_letters and letter not in self.placed_letters: 
                self.excluded_letters.add(letter)
            elif letter_state == '?':
                if letter in self.excluded_letters:
                    self.excluded_letters.remove(letter)
                self.possible_letters.add(letter)
                self.wrong_places[letter_number].add(letter)
            elif letter_state == '+':
                if letter in self.excluded_letters:
                    self.excluded_letters.remove(letter)
                self.placed_letters[letter_number] = letter
                self.possible_letters.add(letter)

        self.excludeUnsuitableWords()

    def isSuitable(self, word):
        for excluded_letter in self.excluded_letters:
            if excluded_letter in word: return False

        for unplaced_letter in self.possible_letters:
            if unplaced_letter not in word: return False

        for letter, placed_letter in zip(word, self.placed_letters):
            if placed_letter != None and letter != placed_letter: return False

        for letter, displaced_letter in zip(word, self.wrong_places):
            if letter in displaced_letter: return False

        return True

    def excludeUnsuitableWords(self):
        suitable_words = []
        for word in self.words:
            if self.isSuitable(word) and word not in self.excluded_words: 
                suitable_words.append(word)

        self.words = suitable_words
        self.words_count = len(self.words)

    @classmethod
    def getDefinition(cls, word):
        return cls.all_words[word]['definition']

