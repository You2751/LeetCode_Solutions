class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        result = 0
        dic = defaultdict(list)
        for idx, num in enumerate(nums):
            dic[num].append(idx)
        for key, lst in dic.items():

            if((len(lst) > 1 and all(lst[i] - lst[i - 1] == 1 for i in range(1, len(lst)))) or len(lst) == 1):
                result += 1
        return result
