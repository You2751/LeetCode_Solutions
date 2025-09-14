class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        houses.sort()
        heaters.sort()
        idx = 0
        radius = float('-inf')
        distance = float('inf')
        for house in houses:
            while(idx + 1 < n and abs(house - heaters[idx]) >= abs(house - heaters[idx + 1])):
                idx += 1
            distance = abs(house - heaters[idx])
            radius = max(radius, distance)
        return radius