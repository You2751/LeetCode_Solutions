class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        idx = radius = 0
        for house in houses:
            while(idx + 1 < n and abs(house - heaters[idx + 1]) <= abs(house - heaters[idx])):
                idx += 1
            distance = abs(house - heaters[idx])
            radius = max(radius, distance)
        return radius