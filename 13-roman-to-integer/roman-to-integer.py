class Solution:
    def romanToInt(self, s: str) -> int:

        roman2int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        roman_before = {"I": {"V":4, "X": 9}, "X":{"L":40, "C": 90}, "C":{"D":400, "M":900}}

        i = 0
        result = 0
        while i<len(s):
            if s[i] in roman_before and i+1<len(s) and s[i+1] in roman_before[s[i]]:
                result += roman_before[s[i]][s[i+1]]
                i += 2
                continue
            result += roman2int[s[i]]
            i += 1
        return result

            
        