class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = len(s)
        result = [0] * len(s)
        for idx, ch in enumerate(s):
            if(ch == c):
                prev = idx
            result[idx] = abs(idx - prev)
        for idx in range(len(s) - 1, -1, -1):
            if(s[idx] == c):
                prev = idx
            result[idx] = min(result[idx], abs(idx - prev))
        return result