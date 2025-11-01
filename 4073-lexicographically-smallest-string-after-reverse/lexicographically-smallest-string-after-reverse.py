class Solution:
    def lexSmallest(self, s: str) -> str:
        result = min(s, s[::-1])
        n = len(s)
        for k in range(1, n):
            reverse_start = s[:k][::-1] + s[k:]
            reverse_end = s[:n - k] + s[n-k:][::-1]
            result = min(result, reverse_start,reverse_end)
        return result