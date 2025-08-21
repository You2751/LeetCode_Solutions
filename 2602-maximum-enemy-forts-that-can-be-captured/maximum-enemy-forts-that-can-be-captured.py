class Solution:
    def captureForts(self, forts: List[int]) -> int:
        left = result = 0
        for right in range(len(forts)):
            if(forts[right]):
                if(-1 * forts[left] == forts[right]):
                    result = max(result, right - left - 1)
                left = right
        return result