class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            # seed tortoise & hare
            slow = get_next(i)
            fast = get_next(get_next(i))

            while (
                nums[slow] * nums[fast] > 0 and
                nums[slow] * nums[get_next(fast)] > 0):
                if slow == fast:
                    if slow != get_next(slow):
                        return True
                    else:
                        break

                slow = get_next(slow)
                fast = get_next(get_next(fast))

            j = i
            while nums[j] * nums[get_next(j)] > 0:
                nxt = get_next(j)
                nums[j] = 0
                j = nxt

        return False
