class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) < 2):
            return s
        best_left = best_right = 0
        def check_string(left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return left + 1, right - 1
        for idx in range(len(s)):
            left_odd, right_odd = check_string(idx, idx)
            left_even, right_even = check_string(idx, idx + 1)
            if(right_even - left_even > best_right - best_left):
                best_right = right_even
                best_left = left_even
            if(right_odd - left_odd > best_right - best_left):
                best_right = right_odd
                best_left = left_odd
        return s[best_left:best_right + 1]
        