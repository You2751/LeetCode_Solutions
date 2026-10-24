class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        total = 0
        for idx in range(len(words) - 1):
            n = len(words[idx])
            for idx2 in range(idx + 1, len(words)):
                if(words[idx] == words[idx2][:n] and words[idx] == words[idx2][-n:]):
                    total += 1
        return total 