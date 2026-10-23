class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        n = len(batteryPercentages)
        for i in range(n - 1):
            if(batteryPercentages[i] > 0):
                result += 1
                for j in range(i + 1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        if(batteryPercentages[-1] > 0):
            result += 1
        return result