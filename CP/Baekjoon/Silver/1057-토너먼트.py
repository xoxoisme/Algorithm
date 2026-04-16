N, K, M = map(int, input().split())

result = 0
while K != M:
    K -= K // 2
    M -= M //2
    result += 1

print(result)