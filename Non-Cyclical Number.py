class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squared = 0
        value = 1
        while True:  
            while n > 0:
                value = n % 10
                squared += value ** 2
                n = n // 10
            if squared == 1:
                return True
            elif squared in seen:
                return False
            seen.add(squared)
            value = squared
            n = squared
            squared = 0
        