class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [len(s)] * len(s)
        prev = len(s)
        for idx, char in enumerate(s):
            if(char == c):
                prev = idx
            result[idx] = abs(idx - prev)
        for idx in range(len(s) - 1, -1, -1):
            if(s[idx] == c):
                prev = idx
            result[idx] = min(result[idx], abs(idx - prev))
        return result