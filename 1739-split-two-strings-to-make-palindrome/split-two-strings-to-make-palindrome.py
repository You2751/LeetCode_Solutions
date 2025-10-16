class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a, b) or self.check(b, a)
    def check(self, a, b):
        left, right = 0, len(b) - 1
        while(left < right):
            if(a[left] == b[right]):
                left += 1
                right -= 1
            else:
                break
        return a[left:right + 1] == a[left:right + 1][::-1] or b[left:right + 1] == b[left:right + 1][::-1]