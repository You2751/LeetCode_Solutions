class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * len(code)
        if(not k):
            return result
        for left in range(len(code)):
            if(k > 0):
                for right in range(left + 1, left + k + 1):
                    result[left] += code[(right % n)]
            elif(k < 0):
                for right in range(left + k, left):
                    result[left] += code[(right + n) % n]
        return result
