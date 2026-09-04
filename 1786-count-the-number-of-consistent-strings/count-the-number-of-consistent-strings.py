class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        counter = Counter(allowed)
        for word in words:
            counter_word = Counter(word)
            if(any(c not in counter for c in counter_word.keys())):
                continue
            else:
                result += 1
        return result