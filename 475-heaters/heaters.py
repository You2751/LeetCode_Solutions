class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heater_idx = radius = 0
        for house in houses:
            while(heater_idx + 1 < len(heaters) and abs(heaters[heater_idx] - house) >= abs(heaters[heater_idx + 1] - house)):
                heater_idx += 1
            radius = max(radius, abs(heaters[heater_idx] - house))
        return radius