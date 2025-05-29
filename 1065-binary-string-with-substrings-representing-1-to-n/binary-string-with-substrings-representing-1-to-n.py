class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if(n > len(s) * 2):
            return False
        
        for num in range(1, n + 1):
            binary_num = bin(num)[2:]
            if(binary_num not in s):
                return False
        return True