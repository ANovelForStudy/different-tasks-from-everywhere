class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)
        for i, item in enumerate(word):
            if item.isalpha():
                word[i] = ' '
        return len(set(map(int, " ".join("".join(word).split()).split())))
