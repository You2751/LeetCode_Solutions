class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        dic = defaultdict(int)
        for idx, c in enumerate(s):
            if(c in dic):
                result = max(result, idx - dic[c] - 1)
            else:
                dic[c] = idx
        return result