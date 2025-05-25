class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        shortest_substring = ''
        left = right = count_ones = 0
        while(right < len(s)):
            count_ones += s[right] == '1'
            while(count_ones > k or (left < right and s[left] == '0')):
                count_ones -= s[left] == '1'
                left += 1
            right += 1
            while(count_ones == k and (not shortest_substring or right - left < len(shortest_substring) or (right - left == len(shortest_substring) and s[left:right] < shortest_substring))):
                shortest_substring = s[left:right]
        return shortest_substring