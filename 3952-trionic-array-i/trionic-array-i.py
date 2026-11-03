class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        left_idx = 0
        n = len(nums)
        if(n <= 3):
            return False
        while(left_idx + 1 < n and nums[left_idx + 1] > nums[left_idx]):
            left_idx += 1
        print(left_idx)
        midd_idx = left_idx
        while(midd_idx + 1 < n and nums[midd_idx] > nums[midd_idx + 1]):
            midd_idx += 1
        print(midd_idx)
        right_idx = midd_idx
        while(right_idx + 1 < n and nums[right_idx] < nums[right_idx + 1]):
            right_idx += 1
        return 0 < left_idx < midd_idx < right_idx and right_idx == n - 1