class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        length = max(len(v1), len(v2))

        for i in range(length):
            ch1 = v1[i] if i < len(v1) else 0
            ch2 = v2[i] if i < len(v2) else 0
            if(ch1 == ch2):
                continue
            elif(ch1 > ch2):
                return 1
            else:
                return -1
        return 0