class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return True
        if(len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0 and n):
            flowerbed[0] = 1
            n -= 1
        if(len(flowerbed) >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0 and n):
            flowerbed[-1] = 1
            n -= 1        
        for idx in range(1, len(flowerbed) - 1):
            if(flowerbed[idx] == 0 and flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0 and n):
                n -= 1
                flowerbed[idx] = 1
            if(n == 0):
                return True
        return n == 0