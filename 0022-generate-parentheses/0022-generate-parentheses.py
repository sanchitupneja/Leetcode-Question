from typing import List

class Solution:
    def solve(self, ind: int, brackets: List[str], total: int, result: List[str]):
        if ind >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        
        if total > len(brackets) // 2 or total < 0:
            return 
        
        
        brackets[ind] = "("
        self.solve(ind + 1, brackets, total + 1, result)
        
        
        brackets[ind] = ")"
        self.solve(ind + 1, brackets, total - 1, result)
    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        brackets = [""] * (n * 2)
        self.solve(0, brackets, 0, result)
        return result
