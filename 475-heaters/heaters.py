class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        heaters.sort()
        def find_radius(heaters, house):
            left, right = 0, len(heaters)
            while(left < right):
                mid = (left + right) // 2
                if(heaters[mid] >= house):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        for house in houses:
            idx = find_radius(heaters, house)
            left_radius = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_radius = float('inf') if idx == len(heaters) else heaters[idx] - house

            distance = min(left_radius, right_radius)
            radius = max(radius, distance)
        return radius