def dedupPerm(nums, used, N, sub, result):

    if len(sub) == N:
        result.append(sub[:])
        return
    
    for i in range(N):
        if used[i]:
            continue
        if (not used[i-1]) and (i>0 and (nums[i-1] == nums[i])):
            continue

        sub.append(nums[i])
        used[i] = True
        dedupPerm(nums, used, N, sub, result)
        sub.pop()
        used[i] = False



ar = [49, 73, 58, 30, 72, 44, 78, 23]
n = len(ar)
result = []
sub = []
used = [False]*n

dedupPerm(ar, used, n, sub, result)
# print(result)

maxTotal = -float('inf')
ans = ''
for i in result:
    total = sum(i)
    an = ''.join(map(str,i))
    if an > ans:
        maxTotal = total
        ans = an


print(ans,maxTotal)