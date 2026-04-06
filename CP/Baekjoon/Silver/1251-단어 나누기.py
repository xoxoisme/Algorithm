word = input()
result = []

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        case1 = word[:i][::-1]
        case2 = word[i:j][::-1]
        case3 = word[j:][::-1]
        result.append(case1 + case2 + case3)

print(sorted(result)[0])
