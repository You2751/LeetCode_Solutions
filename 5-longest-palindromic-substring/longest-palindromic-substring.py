class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n < 2):
            return s
        def check_string(left, right):
            while(left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
            return left + 1, right - 1
        best_left = best_right = 0

        for idx in range(len(s)):
            odd_left, odd_right = check_string(idx, idx)
            even_left, even_right = check_string(idx, idx + 1)
            if(odd_right - odd_left > best_right - best_left):
                best_right = odd_right
                best_left = odd_left
            if(even_right - even_left > best_right - best_left):
                best_right = even_right
                best_left = even_left
        return s[best_left:best_right + 1]