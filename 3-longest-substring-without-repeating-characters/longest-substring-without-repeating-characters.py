class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        result = 0
        check = set()
        while(right < len(s)):
            while(s[right]  in check):
                check.remove(s[left])
                left += 1
            check.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        return result