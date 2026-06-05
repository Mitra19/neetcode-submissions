class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        sym_num = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["XD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        for sys, no in reversed(sym_num):
            if num // no:
                count = num // no
                res += (sys * count)
            num %= no
        return res
            
