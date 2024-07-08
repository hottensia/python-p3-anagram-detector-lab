# your code goes here!
class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])

    def match(self, word_list):
        match_word_items = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.letters:
                match_word_items.append(word)

        return match_word_items


