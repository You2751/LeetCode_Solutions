class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = defaultdict(list)
        for idx, num in enumerate(nums):
            dic[num].append(idx)
        for lst in dic.values():
            if(len(lst) >= 2):
                for i in range(len(lst) - 1):
                    if(lst[i + 1] - lst[i] <= k):
                        return True
        return False