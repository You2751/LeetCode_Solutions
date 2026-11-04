class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        total = 0
        max_range = -1
        def get_range(num):
            max_digit = float('-inf')
            min_digit = float('inf')
            while(num):
                digit = num % 10
                num = num // 10
                max_digit = max(max_digit, digit)
                min_digit = min(min_digit, digit)
            return max_digit, min_digit
        for num in nums:
            max_dig, min_dig = get_range(num)
            num_range = max_dig - min_dig
            if(num_range > max_range):
                max_range = num_range
                total = num
            elif(num_range == max_range):
                total += num
        return total