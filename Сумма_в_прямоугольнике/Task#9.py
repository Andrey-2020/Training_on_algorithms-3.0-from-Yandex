# Если реализовать обычным методом, то время O(Q*N^2) = 10^11.
# Поэтому надо использовать префиксные суммы.
# Одномерные суммы дадут сложность O(NQ) = 10^8.
# Поэтому используем двумерные префиксные суммы.
stdin = open('input.txt', 'r')

N, M, K = map(int, stdin.readline().rstrip().split(' '))
array = [[0 for x in range(0, M + 1)]]
for i in range(0, N):
    section = list(map(int, stdin.readline().rstrip().split(' ')))
    j = 0
    array.append([0])
    for number in section:
        j += 1
        array[i+1].append(number)
pref = array.copy()
for i in range(1, N+1):
    for j in range(1, M + 1):
        if (i == 0):
            pref[i][j] = array[i][j] + pref[i][j-1]
        else:
            pref[i][j] = array[i][j] + pref[i-1][j] + \
                pref[i][j-1] - pref[i-1][j-1]
for i in range(0, K):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split(' '))
    sum_in__rec = pref[x2][y2] - pref[x1 - 1][y2] - \
        pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1]
    print(sum_in__rec)

stdin.close()
