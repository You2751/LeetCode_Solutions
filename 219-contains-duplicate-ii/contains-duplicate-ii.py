class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index = {}
        for idx, num in enumerate(nums):
            if(num in nums_index and abs(idx - nums_index[num]) <= k):
                return True
            nums_index[num] = idx
        return False