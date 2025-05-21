class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = result = 0
        for right, ch in enumerate(s):
            while(ch in check):
                check.remove(s[left])
                left += 1
            check.add(ch)
            result = max(result, right - left + 1)
        return result