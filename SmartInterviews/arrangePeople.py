# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

N = int(input())
M = int(input())
ar = list(map(int,input().split()))


people = 0
vacant = 0

last = -1

if len(ar) == 1 and ar[0] == 0:
    people = 1

for i in range(M):
    if ar[i] == 0:
        vacant += 1
    else:
        if vacant > 1 and last == -1:
            people += (vacant//2)
        elif vacant > 2 and (last+vacant) <= M-1:
            people += (vacant-1)//2

        vacant = 0
        last = i

if vacant > 1 and last != -1:
    people += (vacant//2)

if vacant > 1 and last == -1:
    people += (vacant+1)//2

indexArray = []
for i in range(M):
    if ar[i] == 1:
        indexArray.append(i)



if people >= N:
    print("YES")
else:
    print("NO")














# cnt = 0

# indexArray = []
# for i in range(M):
#     if ar[i] == 1:
#         indexArray.append(i)

# last = -1
# prev = 0
# for j in range(len(indexArray)):
#     if (indexArray[j] - (prev+1)) > 2:
#         cnt += abs(((indexArray[j]-last)-1)//2)
#     last = indexArray[j]
#     prev = indexArray[j]
#     # print(cnt)

# if len(indexArray) == 0:
#     cnt += math.ceil(len(ar)/2)



# # print(indexArray,cnt)
# if N == cnt:
#     print('YES')
# else:
#     print('NO')