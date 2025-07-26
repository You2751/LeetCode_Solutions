class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            left, right = 0, len(img) - 1
            while(left <= right):
                img[left], img[right] = 1 ^ img[right], 1 ^ img[left]
                left += 1
                right -= 1
        return image