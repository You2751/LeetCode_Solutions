class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        array = list(s)
        for right in range(0, len(s), 2 * k):
            array[right:right + k] = array[right:right + k][::-1]
        return "".join(array)