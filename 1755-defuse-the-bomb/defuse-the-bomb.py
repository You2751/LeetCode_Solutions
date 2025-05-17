class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if(not k):
            return result
        for i in range(len(code)):
            if(k > 0):
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]
        return result