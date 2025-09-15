class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums) / len(nums)
        counter = Counter(nums)
        counter[average] += 1
        num = 1
        while(True):
            if(num > average and num not in counter):
                return num
            else:
                num += 1