class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        print()
        
        xora = 0
        array = []
        for i in range(1,len(A)+1):
            xora = xora ^ i ^ A[i-1]
            array.append(i)
            
        finalList = list(A)+array
            
        setBitIdx = 0
        while(xora>0):
            if xora&1 == 1:
                break
                
            setBitIdx += 1
            xora = xora >> 1
            
        one = []
        zero = []
        for i in finalList:
            if i >> setBitIdx & 1 == 1:
                one.append(i)
            else:
                zero.append(i)
                
        output = []
        one_xor = 0
        for j in one:
            one_xor^=j
        
        zeroXor = 0
        for k in zero:
            zeroXor^=k
            
        final = False    
        for m in A:
            if m == one_xor:
                final = True
                output.append(one_xor)
                break
                
        if final:
            output.append(zeroXor)
            
        else:
            output.append(zeroXor)
            output.append(one_xor)
            
        return output
            
            
            
sol = Solution()
print(sol.repeatedNumber((3, 1, 2, 5, 3)))


        
            
                
                
                
            
        
            
            
                
            
        
            
            
    
            
        
        
        
        
        
        
