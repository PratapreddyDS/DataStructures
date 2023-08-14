
def printSubsequencesSumCount(ar, emtyArr, id, N, k, s):

    if id >= N:
        if s == k:
            return 1
        else:
            return 0

    emtyArr.append(ar[id])
    s += ar[id]
    left  = printSubsequencesSumCount(ar,emtyArr,id+1,N, k, s)
    s -= emtyArr[-1]
    emtyArr.pop()
    right = printSubsequencesSumCount(ar,emtyArr, id+1, N,k, s)
    return left + right


arr = [1,2,1]
emptyArray = []
N = 3
idx = 0
k = 2
s = 0 
print(printSubsequencesSumCount(arr, emptyArray, idx, N, k, s))


def printSubsequencesSum(ar, emtyArr, id, N, k, s):

    if id >= N:
        if s == k:
            print(emtyArr)
        return 

    emtyArr.append(ar[id])
    s += ar[id]
    printSubsequencesSum(ar,emtyArr,id+1,N, k, s)
    s -= emtyArr[-1]
    emtyArr.pop()
    printSubsequencesSum(ar,emtyArr, id+1, N,k, s)
    return


arr = [1,2,1]
emptyArray = []
N = 3
idx = 0
k = 2
s = 0 
printSubsequencesSum(arr, emptyArray, idx, N, k, s)

def printSubsequences(arr,emptyArray,idx,N):


    if idx >= N:
        print(emptyArray)
        return emptyArray

    emptyArray.append(arr[idx])
    printSubsequences(arr,emptyArray,idx+1,N)
    emptyArray.pop()
    printSubsequences(arr,emptyArray, idx+1, N)

    return

arr = [3,1,2]
emptyArray = []
N = 3
idx = 0
printSubsequences(arr,emptyArray,idx,N)