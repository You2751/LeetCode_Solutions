class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        check = set()
        left = result = 0
        for right in range(len(s)):
            while(s[right] in check):
                check.remove(s[left])
                left += 1
            check.add(s[right])
            result = max(result, right - left + 1)
        return result