#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def permutations(lst, used, ar, final):
    
    if len(ar) == len(lst):
        final.append(ar[:])
        return

    for i in range(len(lst)):
        if not used[i]:
            ar.append(lst[i])
            used[i] = True
            permutations(lst, used, ar, final)
            ar.pop()
            used[i] = False
            
            
def checkMagicSquare(lst, n):
    
    for i in range(n):
        if sum(lst[i*n:(i+1)*n]) != 15:
            return False
    
        if sum(lst[i::n]) != 15:
            return False
            
    if sum(lst[0::n+1]) != 15:
        return False
        
    if sum(lst[n-1:n*n-1:n-1]) != 15:
        return False
        
    return True
        
        

magicSquares = []
la = [i for i in range(1, 10)]
used = [False]*len(la)
ar = []
final = []
permutations(la, used, ar, final)
# print(final)

for ea in final:
    if checkMagicSquare(ea, 3):
        print(ea)
        magicSquares.append(ea)
        
        
        
def checkDiff(lst1, lst2):
    f = 0
    for i in range(len(lst1)):
        f += abs(lst1[i]-lst2[i])
    return f
    
def formingMagicSquare(s):
    # Write your code here
    
    l = []
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            l.append(s[i][j])
            
    
    minn = float('inf')
    
    for m in magicSquares:
        x = checkDiff(m, l)
        print(x,m,l)
        minn = min(x, minn)
        
    return minn
    
            
s = [[4,8,2],[4,5,7],[6,1,6]]


print(formingMagicSquare(s))
    


