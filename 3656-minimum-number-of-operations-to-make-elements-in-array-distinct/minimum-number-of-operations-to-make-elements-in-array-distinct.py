class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for idx in range(len(nums) - 1, -1, -1):
            if(nums[idx] in counter):
                return math.ceil((idx + 1) / 3)
            counter[nums[idx]] += 1
        return 0