import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub("\/+", "/", path)
        path = path.split("/")
        new_path = []
        for i in range(len(path)):
            if path[i] == "..":
                if len(new_path)>0:
                    new_path.pop()
                continue
            if path[i] == "." or path[i] == "":
                continue
            new_path.append(path[i])
        return "/"+"/".join(new_path)

