import sys

n = int(input())
heights = list(map(int, input().split()))
res = [0] * n

for i in range(n - 1):
    tmp = -sys.maxsize
    for j in range(i + 1, n):
        if tmp < (heights[j] - heights[i]) / (j - i):
            res[i] += 1
            res[j] += 1
            tmp = (heights[j] - heights[i]) / (j - i)

print(max(res))