class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        result = 0
        if(len(colors) <= 2):
            return 0
        for i in range(1, len(colors) - 1):
            if(colors[i] != colors[i - 1] and colors[i] != colors[i + 1]):
                result += 1
        if(colors[0] != colors[-1] and colors[-1] != colors[-2]):
            result += 1
        if(colors[1] != colors[0] and colors[0] != colors[-1]):
            result += 1
        return result