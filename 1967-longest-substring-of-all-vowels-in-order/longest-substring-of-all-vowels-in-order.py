class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        check = set()
        left = result = 0
        for right, char in enumerate(word):
            if(right > 0 and char < word[right - 1]):
                check.clear()
                left = right
            check.add(char)
            if(len(check) == 5):
                result = max(result, right - left + 1)
        return result