class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bisect(heaters, target):
            left, right = 0, len(heaters) - 1
            while(left < right):
                mid = (left + right) // 2
                if(heaters[mid] >= target):
                    right = mid
                else:
                    left = mid + 1
            return left
        heaters.sort()
        radius = 0
        for house in houses:
            idx = bisect(heaters, house)
            left_distance = float('inf') if idx == 0 else abs(heaters[idx - 1] - house)
            right_distance = float('inf') if idx == len(heaters) else abs(heaters[idx] - house)
            distance = min(left_distance, right_distance)
            radius = max(radius, distance)
        
        return radius
                