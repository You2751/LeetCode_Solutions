class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)
        while(idx + 1 < n and nums[idx + 1] > nums[idx]):
            idx += 1
        result = n - idx - 1
        if(idx == n - 1):
            return 0
        new_arr = nums[idx + 1:] + nums[:idx + 1]
        check_sorted = self.is_sorted(new_arr)
        if(check_sorted):
            return result 
        return -1
    def is_sorted(self, arr):
        for i in range(1, len(arr)):
            if(arr[i] <= arr[i - 1]):
                return False
        return True