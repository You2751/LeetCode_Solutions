class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = result = 0
        check = set()
        for right, c in enumerate(s):
            while(s[right] in check):
                check.remove(s[left])
                left += 1
            check.add(s[right])
            result = max(result, right - left + 1)
        return result