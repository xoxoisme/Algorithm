import sys

N = int(sys.stdin.readline())
ans = abs(100 - N)
M = int(sys.stdin.readline())
if M:
    broken = set(sys.stdin.readline().split())
else:
    broken = set()


for num in range(1000001): 
    for digit in str(num):
        if digit in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)