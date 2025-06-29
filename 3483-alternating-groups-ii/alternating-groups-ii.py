class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        left = result = 0
        for right in range(n + k - 1):
            if(right > 0 and colors[right % n] == colors[(right - 1) % n]):
                left = right
            if(right - left + 1 == k):
                result += 1
                left += 1
        return result
        