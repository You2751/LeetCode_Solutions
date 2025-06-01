class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        result = left = 0
        if(len(word1) < len(word2)):
            return 0
        count_word2 = Counter(word2)
        required_chars = len(count_word2)
        window_counter = defaultdict(int)
        for right, char in enumerate(word1):
            window_counter[char] += 1
            if(window_counter[char] == count_word2[char]):
                required_chars -= 1
            while(required_chars == 0):
                if(count_word2[word1[left]] == window_counter[word1[left]]):
                    required_chars += 1
                window_counter[word1[left]] -= 1
                left += 1
            result += left
        return result