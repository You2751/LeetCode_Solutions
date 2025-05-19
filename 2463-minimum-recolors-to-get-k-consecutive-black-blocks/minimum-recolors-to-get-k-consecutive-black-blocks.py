class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        result = white = s[:k].count("W")
        for i in range(k, len(s)):
            white += 1 if s[i] == 'W' else 0
            white -= 1 if s[i - k] == 'W' else 0
            result = min(result, white)
        return result