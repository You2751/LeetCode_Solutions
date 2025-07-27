class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def prime(num):
            if(num <= 1):
                return False
            for val in range(2, int(sqrt(num)) + 1):
                if(num % val == 0):
                    return False
            return True
        prime_array = []
        array = []
        for idx, num in enumerate(nums):
            if(prime(idx)):
                prime_array.append(num)
            else:
                array.append(num)
        return abs(sum(array) - sum(prime_array))