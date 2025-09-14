class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        n = len(chars)
        while(right < n):
            count = 0
            char = chars[right]
            while(right < n and chars[right] == char):
                right += 1
                count += 1
            chars[left] = char
            left += 1
            if(count > 1):
                for num in str(count):
                    chars[left] = num
                    left += 1
        return left