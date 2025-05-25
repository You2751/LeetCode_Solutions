class Solution:
    def maxRepOpt1(self, text: str) -> int:
        left = max_length = 0
        counter = Counter(text)
        while(left < len(text)):
            curr_idx = left
            while(curr_idx < len(text) and text[left] == text[curr_idx]):
                curr_idx += 1
            left_block = curr_idx - left
            next_idx = curr_idx + 1
            while(next_idx < len(text) and text[next_idx] == text[left]):
                next_idx += 1
            right_block = next_idx - curr_idx - 1
            max_possible = min(left_block + right_block + 1, counter[text[left]])
            max_length = max(max_length, max_possible)
            max_length = max(max_length, left_block)
            left = curr_idx
        return max_length
            