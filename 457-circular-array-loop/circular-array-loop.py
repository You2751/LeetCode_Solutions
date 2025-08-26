class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def get_next_index(index):
            return (index + nums[index]) % n
        for i in range(len(nums)):
            if(nums[i] == 0):
                continue
            slow = i
            fast = get_next_index(i)
            while(nums[slow] * nums[fast] > 0 and nums[slow] * nums[get_next_index(fast)] > 0):
                if(slow == fast):
                    if(slow == get_next_index(slow)):
                        break
                    else:
                        return True
                slow = get_next_index(slow)
                fast = get_next_index(get_next_index(fast))

            index = i
            while(nums[index] * nums[get_next_index(index)] > 0):
                next_index = get_next_index(index)
                nums[index] = 0
                index = next_index
        return False