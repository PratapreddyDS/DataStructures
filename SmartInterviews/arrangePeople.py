import math

# N = int(input())
# M = int(input())
# ar = list(map(int,input().split()))

N = 4
M = 7
ar = [0,0,1,0,0,0,0]


cnt = 0


if sum(ar) == 0:
    cnt += math.ceil(ar/2)


else:


    indexArray = []
    for i in range(M):
        if ar[i] == 1:
            indexArray.append(i)


    last = -1
    for j in range(len(indexArray)):
        cnt += ((indexArray[j]-last)-1)//2
        last = indexArray[j]
        print(cnt)

    if  M - indexArray[-1] > 1:
        cnt += (M - indexArray[-1])//2
        print(cnt, (M - indexArray[-1])//2)

    cnt += len(indexArray)


# print(indexArray,cnt)
if N == cnt:
    print('YES')
else:
    print('NO')