# def merge(A, B):
    
#     temp = []
#     i = 0
#     j = 0

#     idx = len(A)

#     for i in B:
#         A.append(i)

#     i = 0
#     while(idx<len(A)):
#         key = idx
#         while(key>0):
#             if A[key] < A[key-1]:
#                 A[key],A[key-1] = A[key-1],A[key]
#             else:
#                 break
            
#             key -= 1
#         idx += 1






    
    
    

# def merge( A, B):
#     temp = []
#     i = 0
#     j = 0
    
    
#     while(i<len(A) and j < len(B)):
        
#         if A[i] < B [j]:
#             temp.append(A[i])
#             i += 1
#         else:
#             temp.append(B[j])
#             j += 1
            
#     print(temp,i,j)   
#     while(i<len(A)):
#         temp.append(A[i])
#         i += 1
        
#     while(j<len(B)):
#         print('coming',j)
#         temp.append(B[j])
#         j += 1
        
#     A = A+B
#     print(A,temp,len(temp))
#     for k in range(len(A)):
#         # print(i)
        
#         A[k] = temp[k]




def merge(A, B):
    
    p1 = len(A)-1
    p2 = len(B)-1
    p3 = len(A)+len(B) - 1
    
    A = A+B
    print("a",A)
    while(p1>=0 and p2>=0):
        
        if A[p1] > B[p2]:
            A[p3]=A[p1]
            p1 -= 1
            
        else:
            A[p3] = B[p2]
            p2 -= 1
            
        p3 -= 1
        
    
    while(p1>=0):
        A[p3] = A[p1]
        p1 -= 1
        p3 -= 1
        
    while(p2>=0):
        A[p3] = B[p2]
        p2 -= 1
        p3 -= 1

    
    print("egooo",A)



A = [1,7,8]
B = [2,3]
# print(A)
merge(A,B)
print(A)
