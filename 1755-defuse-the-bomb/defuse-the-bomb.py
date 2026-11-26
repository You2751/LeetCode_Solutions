class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0] * n
        if(not k):
            return result
        for left in range(n):
            if(k > 0):
                for right in range(left + 1, left + k + 1):
                    result[left] += code[right % n]
            else:
                for right in range(left + k, left):
                    result[left] += code[(right + n) % n]
        return result