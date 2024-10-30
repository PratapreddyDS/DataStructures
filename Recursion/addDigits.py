class Solution:
    def addDigits(self, num: int) -> int:
        
        if num<10:
            return num
        
        while(num>9):
            ans = 0
            while(num>9):
                ans = ans + num%10
                num = num//10
                if num< 10:
                    ans = ans + num
            num = ans
        return num

class Solution:
    
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            return num
        ans = 0
        while(num>9):
            ans = ans + num%10
            num = num//10
            if num< 10:
                ans = ans + num
                
        return self.addDigits(ans)
        
        
  