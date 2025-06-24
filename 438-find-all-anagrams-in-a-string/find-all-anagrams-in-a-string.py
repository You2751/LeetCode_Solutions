class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(p) > len(s)):
            return []
    
        result = []
        window = len(p)
        counter = Counter(p)
        counter_check = Counter(s[:window])
        if(counter == counter_check):
            result.append(0)
        for right in range(1, len(s) - window + 1):
            counter_check[s[right - 1]] -= 1
            counter_check[s[right + window - 1]] += 1
            if(counter_check[s[right - 1]] == 0):
                del counter_check[s[right - 1]]
            if(counter == counter_check):
                result.append(right)
        return result