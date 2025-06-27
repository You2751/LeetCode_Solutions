class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = result = 0
        max_num = max(nums)
        counter = 0
        for right, num in enumerate(nums):
            if(num == max_num):
                counter += 1
            while(counter >= k):
                result += len(nums) - right
                counter -= 1 if nums[left] == max_num else 0
                left += 1
        return result
            