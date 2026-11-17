class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            else:
                visited.add(n)
                n = self.sumSquares(n)
            
        return False




    def sumSquares(self, n: int) -> int:
        res = 0
        n = str(n)
        for dig in n:
            dig = int(dig)
            res += (dig*dig)
        
        return res
        