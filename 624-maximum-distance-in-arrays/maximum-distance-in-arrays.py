class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        for arr in arrays[1:]:
            result = max(result, abs(arr[-1] - min_val), abs(arr[0] - max_val))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return result