class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = list(zip(labels,values))
        arr.sort(key = lambda x:x[1], reverse = True)
        counter = defaultdict(int)
        picked = score = 0
        for label, value in arr:
            if(picked == numWanted):
                break
            if(counter[label] < useLimit):
                counter[label] += 1
                score += value
                picked += 1
        return score