class Solution:
    def lexSmallest(self, s: str) -> str:
        result = s
        n = len(s)
        for k in range(1, n + 1):
            reverse_start = s[:k][::-1] + s[k:]
            reverse_end = s[:n - k] + s[n-k:][::-1]
            result = min(result, reverse_start,reverse_end)
        return result