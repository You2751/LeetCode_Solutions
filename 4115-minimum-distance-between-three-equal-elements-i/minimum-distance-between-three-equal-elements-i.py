class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = float('inf')
        dic = defaultdict(list)
        for idx, num in enumerate(nums):
            dic[num].append(idx)
        for key, lst in dic.items():
            idx = 0
            print(lst)
            if(len(lst) >= 3):
                for idx in range(2, len(lst)):
                    diff = abs(lst[idx] - lst[idx - 1]) + abs(lst[idx] - lst[idx - 2]) + abs(lst[idx - 1] - lst[idx - 2])
                    result = min(result, diff)
        if(result == float('inf')):
            return -1
        return result