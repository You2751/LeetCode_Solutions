class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        string = haystack[:window]
        if(string == needle):
            return 0
        for right in range(window, len(haystack)):
            string = string[1:] + haystack[right]
            if(string == needle):
                print(haystack[right - window + 1])
                return right - window + 1
        return -1