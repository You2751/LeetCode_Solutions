class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        counter = Counter(s[:3])
        if(len(counter) == 3):
            result += 1
        for idx in range(3, len(s)):
            counter[s[idx]] += 1
            counter[s[idx - 3]] -= 1
            if(counter[s[idx - 3]] == 0):
                del counter[s[idx - 3]]
            if(len(counter) == 3):
                result += 1
        return result