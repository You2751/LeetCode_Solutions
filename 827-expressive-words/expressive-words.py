class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def can_stretch(original, word):
            ptr1 = ptr2 = 0
            while(ptr1 < len(original) and ptr2 < len(word)):
                if(original[ptr1] != word[ptr2]):
                    return False
                
                original_ptr = ptr1
                while(ptr1 < len(original) and original[ptr1] == original[original_ptr]):
                    ptr1 += 1
                original_stretch = ptr1 - original_ptr

                word_ptr = ptr2
                while(ptr2 < len(word) and word[ptr2] == word[word_ptr]):
                    ptr2 += 1
                word_stretch = ptr2 - word_ptr

                if(original_stretch < word_stretch or (original_stretch == 2 and original_stretch > word_stretch)):
                    return False
            return ptr1 == len(original) and ptr2 == len(word)
        return sum(can_stretch(s, word) for word in words)