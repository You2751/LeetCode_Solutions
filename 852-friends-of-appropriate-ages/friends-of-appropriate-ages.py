class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        requests = 0
        counter = Counter(ages)
        sorted_counter = sorted(counter)
        for ageA in sorted_counter:
            for ageB in sorted_counter:
                if(ageB <= (ageA * 0.5) + 7 or ageB > ageA or ageB > 100 and ageA < 100):
                    continue
                requests += counter[ageA] * counter[ageB]
                if(ageB == ageA):
                    requests -= counter[ageA]
                    
        return requests