class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if(start.replace('X', '') != result.replace('X', '')):
            return False
        start_idxs_L = [idx for idx, val in enumerate(start) if val == 'L']
        start_idxs_R = [idx for idx, val in enumerate(start) if val == 'R']
        result_idxs_L = [idx for idx, val in enumerate(result) if val == 'L']
        result_idxs_R = [idx for idx, val in enumerate(result) if val == 'R']       
        
        for l in range(len(start_idxs_L)):
            if(start_idxs_L[l] < result_idxs_L[l]):
                return False
        for r in range(len(start_idxs_R)):
            if(start_idxs_R[r] > result_idxs_R[r]):
                return False
        return True