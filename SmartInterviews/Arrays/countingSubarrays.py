def solve( A, B):
    
    # A.sort()
    i = 0 
    j = 1
    currentSum = 0
    count = 0
    
    while(i<=j and j<len(A)+1):
        
        if sum(A[i:j]) < B:
            count = count + len(A[i:j])
            j += 1
            print(count,j,sum(A[i:j]))

        else:
            print("i",i)
            i += 1
            
            
    print('count',count)      
    return count


print(solve([8,5,1,10,5],20))