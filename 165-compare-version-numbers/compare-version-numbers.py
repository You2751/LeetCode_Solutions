class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        for val1, val2 in zip_longest(version1, version2, fillvalue = "0"):
            val1 = int(val1)
            val2 = int(val2)
            if(val1 == val2):
                continue
            if(val1 > val2):
                return 1
            else:
                return -1
        return 0