class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2)
        swaps = 0
        if(counter_s1 == counter_s2):
            for i in range(len(s1)):
                if(s1[i] != s2[i]):
                    swaps += 1
                    if(swaps / 2 > 1):
                        return False
        else:
            return False
        return True