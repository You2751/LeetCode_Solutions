class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        check_set = set(nums)
        min_val, max_val = min(nums), max(nums)
        for val in range(min_val, max_val + 1):
            if(val not in check_set):
                result.append(val)
        return result