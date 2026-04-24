import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        self.contains = False

        def dfs(r, c, remaining):
            if len(remaining) == 0:
                self.contains = True
                return
            
            if r<0 or r>=m or c<0 or c>=n or board[r][c] == "-1":
                return

            if board[r][c] != remaining[0]:
                return

            board_temp = board[r][c]
            board[r][c] = "-1"

            dfs(r+1, c, remaining[1:])
            dfs(r-1, c, remaining[1:])
            dfs(r, c+1, remaining[1:])
            dfs(r, c-1, remaining[1:])

            board[r][c] = board_temp

        for i in range(m):
            for j in range(n):
                if self.contains:
                    return True
                dfs(i,j,word)
        return self.contains