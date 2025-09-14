class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        n = len(chars)
        while(right < n):
            char = chars[right]
            count = 0
            while(right < n and chars[right] == char):
                count += 1
                right += 1
            chars[left] = char
            left += 1
            if(count > 1):
                for ch in str(count):
                    chars[left] = ch
                    left += 1
        return left