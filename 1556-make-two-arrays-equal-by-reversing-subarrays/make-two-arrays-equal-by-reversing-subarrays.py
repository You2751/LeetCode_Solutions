class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        counter_target = Counter(target)
        counter_arr = Counter(arr)
        for num in arr:
            if(num not in counter_target or counter_arr[num] > counter_target[num]):
                return False
            
        return True