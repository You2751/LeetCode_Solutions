class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_length = zeros = 0
        for right in range(len(nums)):
            if(nums[right] == 0):
                zeros += 1
            while(zeros > k):
                if(nums[left] == 0):
                    zeros -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length 