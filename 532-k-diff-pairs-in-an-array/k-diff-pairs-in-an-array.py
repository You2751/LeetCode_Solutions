class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if(k < 0):
            return 0
        result = 0
        nums.sort()
        n = len(nums)
        left, right = 0, 1
        while(right < n):
            if(left == right):
                right += 1
                continue 
            diff = nums[right] - nums[left]
            if(diff < k):
                right += 1
            elif(diff > k):
                left += 1
            else:
                result += 1
                left += 1
                while(left < right and nums[left] == nums[left - 1]):
                    left += 1
                while(right < n and nums[right] == nums[right - 1]):
                    right += 1
        return result

