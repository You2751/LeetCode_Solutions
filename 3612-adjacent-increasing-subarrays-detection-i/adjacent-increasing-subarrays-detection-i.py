class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def check(idx):
            if(idx + k > n):
                return False
            counter = k - 1
            while(idx + 1 < n and counter):
                if(nums[idx + 1] <= nums[idx]):
                    return False
                idx += 1
                counter -= 1
            return True
        
        for idx in range(0, len(nums)):
            if(check(idx) and check(idx + k)):
                return True
        return False