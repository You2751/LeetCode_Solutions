class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def can_stretch(original, word):
            ptr1 = ptr2 = 0
            while(ptr1 < len(original) and ptr2 < len(word)):
                if(original[ptr1] != word[ptr2]):
                    return False
                original_ptr1 = ptr1
                while(ptr1 < len(original) and original[ptr1] == original[original_ptr1]):
                    ptr1 += 1
                stretch_original = ptr1 - original_ptr1
                word_ptr2 = ptr2
                while(ptr2 < len(word) and word[ptr2] == word[word_ptr2]):
                    ptr2 +=1 
                stretch_word = ptr2 - word_ptr2

                if((stretch_word > stretch_original) or (stretch_original < 3 and stretch_original != stretch_word)):
                    return False
            return ptr1 == len(original) and ptr2 == len(word)
        return sum(can_stretch(s, word) for word in words)