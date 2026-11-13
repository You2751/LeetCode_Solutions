class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        check_set = set()
        for num in arr1:
            while(num):
                check_set.add(num)
                num //= 10
        for num in arr2:
            while(num):
                if(num in check_set):
                    result = max(result, len(str(num)))
                num //= 10
        return result