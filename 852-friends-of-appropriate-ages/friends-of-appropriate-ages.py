class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        result = 0
        counter = Counter(ages)
        for ageA in counter:
            for ageB in counter:
                if(ageB > ageA or (ageB > 100 and ageA < 100) or (ageB <= (0.5 * ageA + 7))):
                    continue
                else:
                    result += counter[ageA] * counter[ageB]
                    if(ageA == ageB):
                        result -= counter[ageA]
        return result