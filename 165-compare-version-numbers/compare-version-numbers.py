class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def check_number(num):
            result = []
            num = num.split('.') 
            for n in num:
                result.append(int(n))
            return result
        v1 = check_number(version1)
        v2 = check_number(version2)
        length = max(len(v1), len(v2))
        
        for i in range(length):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            print(a < b)
            if(a == b):
                continue
            elif(a > b):
                return 1
            elif(a < b):
                return -1
        return 0