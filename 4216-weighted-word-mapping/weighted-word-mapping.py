class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total = 0
            for c in word:
                total += weights[ord(c) - ord('a')] % 26
            idx = total % 26
            result.append(chr(ord('z') - idx))
        return "".join(result)