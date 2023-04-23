# Метод двух указателей
stdin = open('input.txt', 'r')

k = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
chars = set(S)
maxStr = 0
for char in chars:
    fromIndex, lastIndex = 0, 0
    limit = k
    while True:
        for i in range(lastIndex, len(S)):
            if ((not (char == S[i])) and (limit - 1 >= 0)):
                limit -= 1
            elif (not (char == S[i]) and (limit - 1 < 0)):
                break
            maxStr = max(lastIndex - fromIndex, maxStr)
            lastIndex += 1

        fromIndex += 1
        if (lastIndex >= len(S)):
            break
        if not char == S[fromIndex-1]:
            limit += 1
print(maxStr+1)
stdin.close()
