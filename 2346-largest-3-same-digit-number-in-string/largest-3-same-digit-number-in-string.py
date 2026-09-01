class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_result = ""
        prev_max = float('-inf')
        for i in range(1, len(num) - 1):
            if(num[i - 1] == num[i] == num[i + 1]):
                number = num[i - 1] + num[i] + num[i + 1]
                if(int(number) > prev_max):
                    max_result = number
                    prev_max = int(number)
        return max_result