class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def can_heat(radius):
            heater_idx = house_idx = 0
            while(house_idx < len(houses)):
                if(heater_idx >= len(heaters)):
                    return False
                min_range = heaters[heater_idx] - radius
                max_range = heaters[heater_idx] + radius

                if(houses[house_idx] < min_range):
                    return False
                if(houses[house_idx] > max_range):
                    heater_idx += 1
                else:
                    house_idx += 1
            return True
        
        left, right = 0, int(1e9)
        while(left < right):
            mid = (left + right) // 2
            if(can_heat(mid)):
                right = mid
            else:
                left = mid + 1
        return left