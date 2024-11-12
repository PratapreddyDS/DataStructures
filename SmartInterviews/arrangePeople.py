import math

# N = int(input())
# M = int(input())
# ar = list(map(int,input().split()))

# N = 4
# M = 7
# ar = [0,0,1,0,0,0,0]

N = 2
M = 9
ar = [1,0,1,0,0,1,0,0,1]


cnt = 0

indexArray = []
for i in range(M):
    if ar[i] == 1:
        indexArray.append(i)

print(indexArray)

last = -1
prev = 0
for j in range(len(indexArray)):
    if (indexArray[j] - (prev+1)) > 2:
        # print(indexArray[j],prev,indexArray[j] - (prev-1))
        cnt += abs(((indexArray[j]-last)-1)//2)
        print(cnt)
    last = indexArray[j]
    prev = indexArray[j]
    # print(cnt)

if len(indexArray) == 0:
    cnt += math.ceil(len(ar)/2)

# print(indexArray,cnt)
if N == cnt:
    print('YES')
else:
    print('NO')