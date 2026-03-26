class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_map = {"1":"", "2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        solutions = []

        def search(digits: str, solution:str):
            if len(digits) == 0:
                solutions.append(solution)
                return

            for i in digit_map[digits[0]]:
                search(digits[1:], solution+i)

        search(digits, "")

        return solutions
