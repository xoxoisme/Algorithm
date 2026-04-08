N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N):
    if S <= 0:
        break

    max_idx = i
    for j in range(i + 1, min(N, i + S + 1)):
        if arr[j] > arr[max_idx]:
            max_idx = j

    for j in range(max_idx, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]

    S -= (max_idx - i)

print(*arr)