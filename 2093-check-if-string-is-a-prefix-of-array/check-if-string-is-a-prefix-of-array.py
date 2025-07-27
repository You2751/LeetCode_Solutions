class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        string = ""
        for word in words:
            string += word
            if(string == s):
                return True
        return False