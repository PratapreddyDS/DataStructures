# Enter your code here. Read input from STDIN. Print output to STDOUT

def permutations(lst,used,result,final):

    if len(result) == len(lst):
        # print(result)
        final.append(result[:])
        return

    for i in range(len(lst)):
        if used[i] == False:
            result.append(lst[i])
            used[i] = True
            permutations(lst,used,result,final)
            result.pop()
            used[i] = False

    return

def checkMagicSquare(lst,n):
    for i in range(n):
        if sum(lst[i*n:(i+1)*n])%5 != 0:
            return False

        if sum(lst[i::n])%5 != 0:
            return False

    if sum(lst[0::n+1])%5 != 0:
        return False
    if sum(lst[n-1:n*n-1:n-1])%5 != 0:
        return False

    return True


# def checkMagicSquare(lst,n):
#     A = []
#     # print(lst)
#     for i in range(n):
#         s = i*n
#         e = s+n
#         A.append(lst[s:e])
#         if sum(lst[s:e])%5 != 0:
#             return False

#     # print(A)

#     for k in range(n):
#         summ = 0
#         for l in range(n):
#             # print(l,k)
#             summ += A[l][k]

#         if summ%5 != 0:
#             return False

#     dia = 0
#     for d in range(n):
#         dia += A[d][d]

#     if dia%5 != 0:
#         return False


#     rdia = 0
#     p = 0
#     q = n-1
#     while(p<n and q>=0):
#         rdia += A[p][q]
#         p += 1
#         q -= 1

#     if rdia%5 != 0:
#         return False

#     return True



inp = [a for a in range(1,10)]
used = [False]*len(inp)
result = []
final = []


permutations(inp,used,result,final)
allMagic = []
for e in final:
    if checkMagicSquare(e, 3):
        allMagic.append(e)
        print(e)

def checkDiff(lst1,lst2):
    final = 0
    for i in range(len(lst1)):
        final += abs(lst1[i]-lst2[i])

    return final


# t = int(input())

# for _ in range(t):
#     x = list(map(int,input().split()))
#     y = list(map(int,input().split()))
#     z = list(map(int,input().split()))

#     lst = x+y+z

#     if checkMagicSquare(lst,3):
#         print("0")
#     else:
#         mincost = float('inf')
#         for each in allMagic:
#             cst = checkDiff(each,lst)
#             mincost = min(mincost,cst)

#         print(mincost)