class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        dic = defaultdict(int)
        for idx, num in enumerate(arr2):
            dic[num] = idx
        existing_vals, not_existing = [], []
        for num in arr1:
            if(num in dic):
                existing_vals.append(num)
            else:
                not_existing.append(num)
        if(not_existing):
            not_existing.sort()
        existing_vals.sort(key = lambda x:(dic[x]))
        return existing_vals + not_existing