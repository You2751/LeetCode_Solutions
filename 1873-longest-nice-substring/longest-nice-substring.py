class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check_nice(string):
            for c in string:
                if(c.swapcase() not in string):
                    return False
            return True
        window_size = len(s)
        while(window_size):
            for i in range(len(s) - window_size + 1):
                string = s[i:i + window_size]
                if(check_nice(string)):
                    return string
            window_size -= 1
        return ""