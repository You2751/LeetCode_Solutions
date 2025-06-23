class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counter = Counter(p)
        window = len(p)
        counter_check = Counter(s[:window])
        if(counter == counter_check):
            result.append(0)
        for i in range(1, len(s) - window + 1):
            counter_check[s[i - 1]] -= 1
            counter_check[s[i + window - 1]] += 1
            if(counter_check[i - 1] == 0):
                del counter_check[i - 1]
            if(counter == counter_check):
                result.append(i)
        return result