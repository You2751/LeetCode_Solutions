class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next_index(index):
            return (index + nums[index]) % len(nums)
        for i in range(len(nums)):
            if(nums[i] == 0):
                continue
            slow, fast = i, next_index(i)
            while(nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0):
                if(slow == fast):
                    if(slow != next_index(slow)):
                        return True
                    else:
                        break
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            index = i
            while(nums[index] * nums[next_index(index)] > 0):
                next_jump = next_index(index)
                nums[index] = 0
                index = next_jump
        return False