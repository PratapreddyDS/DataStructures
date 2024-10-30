class Solution:
    
    def getSum(self, st):
        d = 0
        for i in st:
            d += int(i)
        
        return str(d)
            
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            currentStr = ""
            
            i = 0
            while i < len(s):
                if len(s) - i >= k:
                    p = self.getSum(s[i:i+k])
                    currentStr += p
                    i += k
                else:
                    p = self.getSum(s[i:len(s)])
                    currentStr += p
                    i = len(s)
            
            s = currentStr
        
        return s
            

sol = Solution()

st = "11111222223"
k =3

print(sol.digitSum(st,k))