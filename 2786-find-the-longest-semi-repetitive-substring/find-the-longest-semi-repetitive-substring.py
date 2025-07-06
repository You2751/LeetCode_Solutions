class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if(len(s) < 2):
            return 1
        left = result = pairs = 0
        for right in range(1, len(s)):
            if(s[right] == s[right - 1]):
                pairs += 1
            while(pairs > 1 and left < right):
                if(s[left] == s[left + 1]):
                    pairs -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
    