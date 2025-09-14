class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next_idx(idx):
            return (idx + nums[idx]) % n
        for i in range(n):
            if(nums[i] == 0):
                continue
            slow = next_idx(i)
            fast = next_idx(next_idx(i))
            while(nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_idx(fast)] > 0):
                if(slow == fast):
                    if(slow != next_idx(slow)):
                        return True
                    break
                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))
            index = i
            while(nums[index] * nums[next_idx(index)] > 0):
                next_index = next_idx(index)
                nums[index] = 0
                index = next_index
        return False