class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check_word(word):
            for ch in word:
                if(ch.swapcase() not in word):
                    return False
            return True
        window_size = len(s)
        while(window_size):
            for i in range(len(s) - window_size + 1):
                string = s[i:i + window_size]
                if(check_word(string)):
                    return string
            window_size -= 1
        return ""