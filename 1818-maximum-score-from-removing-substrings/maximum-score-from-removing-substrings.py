class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        high_priority = 'ab' if x > y else 'ba'
        low_priority = 'ba' if high_priority == 'ab' else 'ab'

        string_high_priority = self.remove_chars(s, high_priority)
        string_high_priority_length = (len(s) - len(string_high_priority)) // 2
        total_points = string_high_priority_length * max(x, y)

        string_low_priority = self.remove_chars(string_high_priority, low_priority)
        string_low_priority_length = (len(string_high_priority) - len(string_low_priority)) // 2
        total_points += string_low_priority_length * min(x, y)
        
        return total_points
    def remove_chars(self, s, target):
        stack = []
        for c in s:
            if(c == target[1] and stack and stack[-1] == target[0]):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


