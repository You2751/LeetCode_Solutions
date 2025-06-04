class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for right, num in enumerate(nums):
            if(num in dic and right - dic[num] <= k):
                return True
            dic[num] = right
        return False