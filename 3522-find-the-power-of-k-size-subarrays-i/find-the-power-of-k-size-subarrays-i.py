class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if(k == 1):
            return nums
        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive = 1
        for i in range(length - 1):
            if(nums[i + 1] == nums[i] + 1):
                consecutive += 1
            else:
                consecutive = 1
            if(consecutive >= k):
                result[i - k + 2] = nums[i + 1]
        return result