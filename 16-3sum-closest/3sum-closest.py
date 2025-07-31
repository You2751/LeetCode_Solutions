class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for idx in range(len(nums) - 2):
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            left, right = idx + 1, len(nums) - 1
            while(left < right):
                check_sum = nums[idx] + nums[left] + nums[right]
                if(check_sum > target):
                    right -= 1
                elif(check_sum < target):
                    left += 1
                else:
                    return check_sum
                if(abs(check_sum - target) < abs(closest_sum - target)):
                    closest_sum = check_sum
        return closest_sum