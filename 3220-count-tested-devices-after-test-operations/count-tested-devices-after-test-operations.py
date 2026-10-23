class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = decrements = 0
        for battery in batteryPercentages:
            if(battery - decrements > 0):
                result += 1
                decrements += 1
        return result