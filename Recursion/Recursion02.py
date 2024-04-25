def nameFiveTimes(inputName,i):

    if i>=5:
        return
    print(f'My name is {inputName}')
    i += 1
    return nameFiveTimes(inputName,i)

# nameFiveTimes("pratap", 0)


def printNumberInLinear(j,N):
    if j>N:
        return
    print(f'count : {j}')
    j+=1
    return printNumberInLinear(j,N)

# printNumberInLinear(1,10)


def printNumberInreverseLinear(k,N):
    if N<k:
        return
    print(f'count rev : {N}')
    N-=1
    return printNumberInreverseLinear(k,N)

# printNumberInreverseLinear(1,10)

def printNumberInLinearBacktrac(m,N):
    
    if m<1:
        return
    # m-=1
    printNumberInLinearBacktrac(m-1,N)
    print(f'count : {m}')

# printNumberInLinearBacktrac(10,10)


def printNumbInBackLineBacktrac(b,N):

    if b>N:
        return
    printNumbInBackLineBacktrac(b+1,N)
    print(f'count : {b}')


printNumbInBackLineBacktrac(1,10)
    



