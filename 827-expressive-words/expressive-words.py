class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def can_stretch(original, word):
            ptr1 = ptr2 = 0
            while(ptr1 < len(original) and ptr2 < len(word)):
                if(original[ptr1] != word[ptr2]):
                    return False
                stretch_orginal_ptr1 = ptr1
                while(ptr1 < len(original) and original[ptr1] == original[stretch_orginal_ptr1]):
                    ptr1 += 1
                stretch_original_length = ptr1 - stretch_orginal_ptr1
                
                stretch_word_ptr2 = ptr2
                while(ptr2 < len(word) and word[stretch_word_ptr2] == word[ptr2]):
                    ptr2 += 1
                stretch_word_length = ptr2 - stretch_word_ptr2

                if(stretch_word_length > stretch_original_length):
                    return False
                if(stretch_original_length < 3 and stretch_word_length != stretch_original_length):
                    return False
            return ptr1 == len(original) and ptr2 == len(word)
        return sum(can_stretch(s, word) for word in words)