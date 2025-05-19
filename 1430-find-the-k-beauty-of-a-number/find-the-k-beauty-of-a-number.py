class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        str_num = str(num)
        initial = str(num)[:k]
        if(num % int(initial) == 0):
            result += 1
        for i in range(k, len(str_num)):
            initial += str_num[i]
            initial = initial[1:]
            print(initial)
            if(int(initial) > 0 and num % int(initial) == 0):
                result += 1
        return result