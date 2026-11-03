class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        coupons = []
        check_dic = {"electronics":1, "grocery":2, "pharmacy":3, "restaurant":4}
        for code, b_line, active in zip(codes,businessLine, isActive):
            if(code != "_"):
                first_condition = code.replace("_", "").isalnum() and (code != "")
            else:
                first_condition = True
            second_condition = active
            if(first_condition and b_line in check_dic and active):
                coupons.append([check_dic[b_line], code])
        coupons.sort()
        return [code for _, code in coupons]