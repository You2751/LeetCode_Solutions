class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for idx in range(len(nums) - 2):
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            left, right = idx + 1, len(nums) - 1
            while(left < right):
                curr_sum = nums[idx] + nums[left] + nums[right]
                if(curr_sum > target):
                    right -= 1
                elif(curr_sum < target):
                    left += 1
                else:
                    return curr_sum
                if(abs(closest_sum - target) > abs(curr_sum - target)):
                    closest_sum = curr_sum
        return closest_sum