class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        idx = 0
        n = len(bits)
        while(idx < n):
            if(idx == n - 1 and bits[idx] == 0):
                return True
            if(bits[idx] == 1):
                if(idx + 2 < n):
                    idx += 2
                else:
                    return False
            else:
                idx += 1
        return False