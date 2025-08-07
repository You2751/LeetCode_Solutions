class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        idx = radius = 0
        
        for house in houses:
            while(idx  + 1< len(heaters) and abs(house - heaters[idx]) >= abs(house - heaters[idx + 1])):
                idx += 1
            distance = abs(house - heaters[idx])
            radius = max(radius, distance)
        return radius
        