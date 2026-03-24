import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
root = -1

for i in range(n):
    if tree[i] == -1:
        root = i
    else:
        graph[tree[i]].append(i)

deleted = [False] * n

def dfs(del_node):
    deleted[del_node] = True
    for child in graph[del_node]:
        dfs(child)

dfs(delete)

cnt = 0
for i in range(n):
    if deleted[i]:
        continue

    is_leaf = True
    for child in graph[i]:
        if not deleted[child]:
            is_leaf = False
            break

    if is_leaf:
        cnt += 1

print(cnt)