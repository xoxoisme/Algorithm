import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
k = int(input())

max_cnt = 0

for row in range(n):
    zero = lst[row].count('0')

    same_rows = 0

    if zero <= k and (k - zero) % 2 == 0:
        for other_row in range(n):
            if lst[row] == lst[other_row]:
                same_rows += 1

    max_cnt = max(max_cnt, same_rows)

print(max_cnt)