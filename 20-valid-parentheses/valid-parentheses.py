class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_chars = {"(":")", "[":"]", "{":"}"}

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if map_chars[last] != c:
                    return False
        if len(stack)>0:
            return False
        return True
