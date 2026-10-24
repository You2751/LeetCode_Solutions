class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        count_odd = count_even = 0
        odd, even = [0] * (n + 1) , [0] * (n + 1)
        for idx in range(n - 1, -1, -1):
            if(nums[idx] % 2):
                count_odd += 1
                odd[idx] = count_odd
                even[idx] = count_even
            else:
                count_even += 1
                even[idx] = count_even
                odd[idx] = count_odd
        print(even)
        print(odd)
        for idx, num in enumerate(nums):
            if(num % 2):
                result[idx] = even[idx + 1]
            else:
                result[idx] = odd[idx + 1]

        return result