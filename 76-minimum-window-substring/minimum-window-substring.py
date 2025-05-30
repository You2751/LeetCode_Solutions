class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        window_counter = defaultdict(int)
        valid_chars = left = 0
        min_size = float('inf')
        min_left = -1
        for right, char in enumerate(s):
            window_counter[char] += 1
            if(target_counter[char] >= window_counter[char]):
                valid_chars += 1
            while(valid_chars == len(t)):
                if(right - left + 1 < min_size):
                    min_size = right - left + 1
                    min_left = left
                if(target_counter[s[left]] >= window_counter[s[left]]):
                    valid_chars -= 1
                window_counter[s[left]] -= 1
                left+=1
        return '' if min_left < 0 else s[min_left:min_left + min_size]