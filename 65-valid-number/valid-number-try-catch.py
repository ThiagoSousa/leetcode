import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        if s in ["inf", "-inf", "+inf", "infinity", "-infinity", "+infinity", "nan", "-nan", "+nan"]:
            return False

        try:
            s = float(s)
            return True
        except:
            return False
