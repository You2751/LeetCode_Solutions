class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        while(right < len(chars)):
            char = chars[right]
            count = 0
            while(right < len(chars) and chars[right] == char):
                count += 1
                right += 1
            chars[left] = char
            left += 1
            if(count > 1):
                for num in str(count):
                    chars[left] = num
                    left += 1
        return left