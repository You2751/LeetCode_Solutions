class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = float('inf')
        for i in range(1, len(nums) - 1):
            left_num = min(nums[:i])
            right_num = min(nums[i + 1:])
            if(left_num < nums[i] > right_num):
                result = min(result, nums[i] + left_num + right_num)
        if(result != float('inf')):
            return result
        return -1