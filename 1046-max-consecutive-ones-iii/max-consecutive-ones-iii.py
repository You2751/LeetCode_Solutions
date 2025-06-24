class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = result = ones = 0
        for right, num in enumerate(nums):
            if(num):
                ones += 1
            else:
                k -= 1
            while(k < 0):
                if(nums[left] == 0):
                    k += 1
                left += 1
            result = max(result, right - left + 1)

        return result 