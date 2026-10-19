class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        result = 0
        dic = defaultdict(list)
        counter = Counter(nums)
        for idx, num in enumerate(nums):
            if(counter[num] == 3):
                dic[num].append(idx)
        for key, lst in dic.items():
            if(lst[1] - lst[0] == lst[2] - lst[1]):
                result += 1
        return result