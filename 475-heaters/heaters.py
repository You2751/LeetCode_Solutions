class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0

        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            left_distance = float('inf') if idx == 0 else abs(house - heaters[idx - 1])
            right_distance = float('inf') if idx == len(heaters) else abs(house - heaters[idx])
            
            distance = min(left_distance, right_distance)
            radius = max(radius, distance)
        return radius