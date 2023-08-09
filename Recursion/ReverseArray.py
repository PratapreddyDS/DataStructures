def reverse(Arr,f,l):

    """ using recursion we are reversing an array"""

    if f >= l:
        return
    Arr[f],Arr[l] = Arr[l],Arr[f]
    reverse(Arr,f+1,l-1)

    return 

Arr = [1,2,3,4]
reverse(Arr,0,3)

print(Arr)



def checkPalindrome(string,f,l):

    if f >= l:
        return True

    if string[f] != string[l]:
        return False

    return checkPalindrome(string,f+1,l-1)


status = checkPalindrome("SMADAMSK", 0, 7)
print(status)