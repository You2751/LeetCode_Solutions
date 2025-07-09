class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = count_ones = 0
        result = None
        for right, char in enumerate(s):
            if(char == '1'):
                count_ones += 1
            while(count_ones >= k):
                string = s[left:right + 1]
                if(result is None or len(string) < len(result) or (len(result) == len(string) and string < result)):
                    result = string
                if(s[left] == '1'):
                    count_ones -= 1
                
                left += 1
        return result if result is not None else ""
