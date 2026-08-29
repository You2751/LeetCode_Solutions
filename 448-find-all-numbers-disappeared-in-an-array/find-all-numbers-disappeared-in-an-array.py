class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        check_set =  set(nums)
        for val in range(1, n + 1):
            if(val not in check_set):
                result.append(val)
        return result