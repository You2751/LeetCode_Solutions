class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        n = len(nums)
        def is_inscreasing(arr):
            for i in range(1, len(arr)):
                if(arr[i] <= arr[i - 1]):
                    return False
            return True

        for i in range(n - 1):
            if(nums[i + 1] <= nums[i]):
                left_arr = nums[:i] + nums[i + 1:]
                right_arr = nums[:i + 1] + nums[i + 2:]
                return is_inscreasing(left_arr) or is_inscreasing(right_arr)
        return True