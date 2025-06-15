class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = result = 0
        counter = Counter(nums)
        sub_counter = defaultdict(int)
        unique_chars = len(counter)
        while(right < len(nums)):
            sub_counter[nums[right]] += 1
            while(len(sub_counter) == unique_chars):
                result += (n - right)
                sub_counter[nums[left]] -= 1
                if(sub_counter[nums[left]] == 0):
                    del sub_counter[nums[left]]
                left += 1
            right += 1
        return result