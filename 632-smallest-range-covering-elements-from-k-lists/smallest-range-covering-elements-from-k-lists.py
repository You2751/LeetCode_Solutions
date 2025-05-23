class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        flat_list = [(val, idx) for idx, lst in enumerate(nums) for val in lst]
        flat_list.sort()
        counter = defaultdict(int)
        result = [float('-inf'), float('inf')]
        left = 0
        for right_val, lst_idx in flat_list:
            counter[lst_idx] += 1
            while(len(counter) == len(nums)):
                left_val = flat_list[left][0]
                size_difference = right_val - left_val - (result[1] - result[0])
                if(size_difference < 0 or (size_difference == 0 and left_val < result[0])):
                    result = [left_val, right_val]
                counter[flat_list[left][1]] -= 1
                if(not counter[flat_list[left][1]]):
                    del counter[flat_list[left][1]]
                left += 1
        return result