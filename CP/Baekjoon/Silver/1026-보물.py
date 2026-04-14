N = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

S = 0
for i in range(N):
    min_a = min(a_arr)
    max_b = max(b_arr)

    S += min_a * max_b
    
    a_arr.pop(a_arr.index(min_a))
    b_arr.pop(b_arr.index(max_b))

print(S)