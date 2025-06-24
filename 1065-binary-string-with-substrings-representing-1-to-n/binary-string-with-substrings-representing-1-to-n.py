class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if(len(bin(n)[2:]) > len(s)):
            return False
        for num in range(1, n + 1):
            binary = bin(num)[2:]
            if(binary not in s):
                return False
        return True