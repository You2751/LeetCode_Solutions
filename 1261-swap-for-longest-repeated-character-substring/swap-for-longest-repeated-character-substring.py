class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = Counter(text)
        left = max_length = 0
        while(left < len(text)):
            curr_idx = left
            while(curr_idx < len(text) and text[curr_idx] == text[left]):
                curr_idx += 1
            left_chunk = curr_idx - left
            next_idx = curr_idx + 1
            while(next_idx < len(text) and text[next_idx] == text[left]):
                next_idx += 1
            right_chunk = next_idx - curr_idx - 1
            max_possible = min(counter[text[left]], left_chunk + right_chunk + 1)
            max_length = max(max_length, max_possible)
            max_length = max(max_length, left_chunk)
            left = curr_idx
        return max_length 