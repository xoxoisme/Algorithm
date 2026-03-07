# 피보나치 수열을 재귀로 구현한 예시이다.
# O(2^n) 시간 복잡도를 가지며, n이 커질수록 계산 시간이 급격히 증가한다.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 피보나치 반복문으로 구현한 예시이다.
# O(n) 시간 복잡도를 가지며, n이 커져도 계산 시간이 선형적으로 증가한다.
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1): # 반복 횟수만 필요해서 _ 사용
        a, b = b, a + b
    return b

# 피보나치 수열을 동적계획법으로 구현한 예시이다.
# O(n) 시간 복잡도를 가지며, n이 커져도 계산 시간이 선형적으로 증가한다.
def finbonacci_dynamic(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

