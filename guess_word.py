# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import collections

class Solution:
    
    def findSecretWord(self, wordlist, master):
        def match(w1, w2):
            return sum(i == j for i, j in zip(w1, w2))

        n = 0
        while n < 6:
            count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(wordlist, key=lambda w: sum(count[i][c] for i, c in enumerate(w)))
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]
        
            
        