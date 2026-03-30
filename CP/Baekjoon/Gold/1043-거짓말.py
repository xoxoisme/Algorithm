import sys

N, M = map(int, sys.stdin.readline().split())
know = set(map(int, sys.stdin.readline().split()[1:]))
participants = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(M)]

for _ in range(M):
    for p in participants:
        if know & p:
            know |= p

count = 0
for p in participants:
    if not know & p:
        count += 1

print(count)