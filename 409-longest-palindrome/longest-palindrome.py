class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        odd = False
        for val in dic.values():
            if(val % 2 == 0):
                result += val
            else:
                odd = True
                result += val - 1
        if(odd):
            return result + 1
        return result