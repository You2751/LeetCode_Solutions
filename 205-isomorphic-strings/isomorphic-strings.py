class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dic1, dic2 = dict(), dict()
        for idx, val in enumerate(s):
            if((val in dic1 and dic1[val] != t[idx]) or (t[idx] in dic2 and dic2[t[idx]] != val)):
                return False
            dic1[val] = t[idx]
            dic2[t[idx]] = val
        return True
                
        