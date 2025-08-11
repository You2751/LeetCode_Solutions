class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        left = right = 0
        while(left < len(groups) and right <= len(nums) - len(groups[left])):
            group = groups[left]
            check_group = nums[right:right + len(group)]
            if(group == check_group):
                right += len(group)
                left += 1
            else:
                right += 1
        return left == len(groups)