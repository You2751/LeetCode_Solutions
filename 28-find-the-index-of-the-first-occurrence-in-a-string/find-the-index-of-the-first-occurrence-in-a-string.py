class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        string = haystack[:window]
        print(string)
        if(string == needle):
            return 0
        for i in range(window, len(haystack)):
            string = string[1:] + haystack[i]
            if(string == needle):
                return i - window + 1
        return -1