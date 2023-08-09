# print names five times using recursion
def printNames(count):
    if count >= 5:
        return
    print("pratap")
    printNames(count+1)
    return
# printNames(0)

# print numbers from N to 1

def printNto1(N):

    if N<0:
        return
    print(N)
    printNto1(N-1)
    return

# printNto1(4)

# printing 1 to 4 with slight modifaction from the above problem
def printNto1(N):

    """
        just placed the print statement right below the function recursion will call the last element first 
        later, reducing one by one. This is similar to Backtracking. 

    """

    if N<0:
        return
    printNto1(N-1)
    print(N)
    return

# printNto1(4)


# print numbers from N to 1 without using N-1, This is like backtracking. 

def printNto1WithoutMinus(N,number):

    if number>N:
        return
    printNto1WithoutMinus(N,number+1)
    print(number)
    return
printNto1WithoutMinus(4,0)



    


    




    





    