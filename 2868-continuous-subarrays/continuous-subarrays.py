class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        left = right = result = 0
        while(right < len(nums)):
            counter[nums[right]] += 1
            while(max(counter) - min(counter) > 2):
                counter[nums[left]] -= 1
                if(counter[nums[left]] == 0):
                    del counter[nums[left]]
                left += 1
            result += right - left + 1
            right += 1
        return result