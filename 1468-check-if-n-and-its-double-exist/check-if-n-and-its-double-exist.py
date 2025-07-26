class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        for val in arr:
            if(val / 2 in dic or val * 2 in dic):
                return True
            dic[val] = True
        return False