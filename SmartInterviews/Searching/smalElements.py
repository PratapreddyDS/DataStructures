def binarySearch(ar,key):
    ar.sort()
    low = 0
    high = len(ar)-1
    count = 0
    while(low<=high):
        mid = (low+high)//2
        # print(mid)
        if ar[mid] >= key:
            high = mid-1
        else:
            low = mid+1
            count = low

    # print(count)  
    return count



ar = [4, 10, 54, 11, 8]

for j in range(len(ar)-1):
    x = binarySearch(ar[j+1:],ar[j])
    print(ar[j],x)