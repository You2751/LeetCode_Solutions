class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if(k == 1):
            return nums
        n = len(nums)
        result = [-1] * (n - k + 1)
        consecutive = 1
        for i in range(len(nums) - 1):
            if(nums[i + 1] == nums[i] + 1):
                consecutive += 1
            else:
                consecutive = 1
            if(consecutive >= k):
                result[i + 1 - (k - 1)] = nums[i + 1]
        return result