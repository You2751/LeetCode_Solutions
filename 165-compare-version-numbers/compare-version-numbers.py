class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1_len = len(v1)
        v2_len = len(v2)
        length = max(v1_len, v2_len)
        for i in range(length):
            v1_num = v1[i] if i < v1_len else 0
            v2_num = v2[i] if i < v2_len else 0
            if(v1_num == v2_num):
                continue
            elif(v1_num > v2_num):
                return 1
            elif(v1_num < v2_num):
                return -1
        return 0