class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for val in arr:
            if(2*val in dic or val / 2 in dic):
                return True
            dic[val] = True
        return False