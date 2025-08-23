class Solution:
    def findIndices(self, nums: List[int], idx_diff: int, valueDifference: int) -> List[int]:
        min_idx = max_idx = 0
        for idx in range(idx_diff, len(nums)):
            diff = idx - idx_diff
            if(nums[diff] < nums[min_idx]):
                min_idx = diff
            if(nums[diff] > nums[max_idx]):
                max_idx = diff
            if(nums[idx] - nums[min_idx] >= valueDifference):
                return [min_idx, idx]
            if(nums[max_idx] - nums[idx] >= valueDifference):
                return [idx, max_idx]
        return [-1, -1]