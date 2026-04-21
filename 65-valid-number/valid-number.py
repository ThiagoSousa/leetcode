import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        if s in ["inf", "-inf", "+inf", "infinity", "-infinity", "+infinity", "nan", "-nan", "+nan", "e", "."]:
            return False

        if re.match("^[\+\-]?((\d+\.\d*)|(\.\d+)|(\d+))([eE][\+\-]?\d+)?$", s):
            return True
        return False
