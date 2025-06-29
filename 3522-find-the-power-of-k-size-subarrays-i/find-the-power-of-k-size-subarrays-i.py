class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if(k == 1):
            return nums
        n = len(nums)
        consecutive = 1
        result = [-1] * (n - k + 1)
        for i in range(n - 1):
            if(nums[i + 1] == nums[i] + 1):
                consecutive += 1
            else:
                consecutive = 1
            if(consecutive >= k):
                result[i - k + 2] = nums[i + 1]
        return result