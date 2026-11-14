class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        n = len(p)
        counter_p = Counter(p)
        dic = Counter(s[:n])
        if(not (counter_p - dic)):
            result.append(0)
        for i in range(n, len(s)):
            dic[s[i]] += 1
            dic[s[i - n]] -= 1
            if(dic[s[i - n]] == 0):
                del dic[s[i - n]]
            if(not(counter_p - dic)):
                result.append(i - n + 1)
        return result