class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = right = count_ones = 0
        shortest_subtring = ''
        while(right < len(s)):
            count_ones += s[right] == '1'
            while(count_ones > k or (left < right and s[left] == '0')):
                count_ones -= s[left] == '1'
                left += 1
            right += 1
            while(count_ones == k and
            (not shortest_subtring) or
            (right - left < len(shortest_subtring)) or
            (right - left == len(shortest_subtring) and s[left:right] < shortest_subtring)):
                shortest_subtring = s[left:right]
        return shortest_subtring