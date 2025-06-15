class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result = 0
        counter = Counter(nums)
        unique_chars = len(counter)
        for left in range(len(nums)):
            unique_set = set()
            for right in range(left, len(nums)):
                unique_set.add(nums[right])
                if(len(unique_set) == unique_chars):
                    result += 1
        return result