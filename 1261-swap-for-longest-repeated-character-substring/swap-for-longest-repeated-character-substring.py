class Solution:
    def maxRepOpt1(self, text: str) -> int:
        result = 0
        counter = Counter(text)
        for char in set(text):
            left = diff = 0
            for right in range(len(text)):
                if(text[right] != char):
                    diff += 1
                while(diff > 1):
                    if(text[left] != char):
                        diff -= 1
                    left += 1
                result = max(result, min(right - left + 1, counter[char]))
        return result