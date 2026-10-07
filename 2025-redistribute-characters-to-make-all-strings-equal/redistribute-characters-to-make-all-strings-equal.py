class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        counter = defaultdict(int)
        for word in words:
            for c in word:
                counter[c] += 1
        for key, val in counter.items():
            if(val % n != 0):
                return False
        return True