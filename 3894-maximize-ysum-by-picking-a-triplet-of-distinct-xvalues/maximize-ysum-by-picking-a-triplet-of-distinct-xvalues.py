class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        counter = Counter(x)
        if(len(counter) < 3):
            return -1
        total = count = 0
        pairs = list(zip(x, y))
        pairs.sort(key = lambda k:k[1], reverse = True)
        seen = set()
        for x1, y1 in pairs:
            if(x1 not in seen):
                seen.add(x1)
                count += 1
                total += y1
                if(count == 3):
                    return total
        return -1