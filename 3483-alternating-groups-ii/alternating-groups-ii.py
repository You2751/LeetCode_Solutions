class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        left = result = 0
        for right, color in enumerate(colors):
            if(right > 0 and colors[right] == colors[right - 1]):
                left = right
            if(right - left + 1 >= k):
                result += 1
        return result