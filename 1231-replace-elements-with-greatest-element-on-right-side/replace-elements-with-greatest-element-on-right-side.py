class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * n
        max_right = arr[-1]
        for i in range(n - 2, -1, -1):
            result[i] = max_right
            max_right = max(max_right, arr[i])
        return result