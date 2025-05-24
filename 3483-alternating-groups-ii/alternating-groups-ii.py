class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        left, right, result = 0, 1, 0
        while(right < len(colors)):
            if(colors[right] == colors[right - 1]):
                left = right
                right += 1
                continue 
            if(right - left < k):
                right += 1
            
            if(right - left >= k):
                result += 1
                left += 1
        return result