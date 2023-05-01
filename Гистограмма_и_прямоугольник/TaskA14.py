stdin = open('input.txt', 'r')

lst = list(map(int, stdin.readline().rstrip().split(' ')))
N = lst[0]


def search_less(isLess_right: bool = True) -> dict:
    """Поиск ближайшего меньшего"""
    stack = []
    less_indx = {}
    if (isLess_right):
        iterator = range(1, N + 1)
    else:
        iterator = range(N, 0, -1)

    for i in iterator:
        hi = lst[i]
        if (not len(stack)):
            stack.append([i, hi])
        elif (len(stack) and stack[-1][1] > hi):
            while len(stack) and stack[-1][1] > hi:
                hj = stack.pop()
                less_indx[hj[0]] = i
            stack.append([i, hi])
        elif (len(stack) and stack[-1][1] <= hi):
            stack.append([i, hi])

    if (len(stack)):
        for hj in stack:
            if (isLess_right):
                less_indx[hj[0]] = N + 1
            else:
                less_indx[hj[0]] = 0
    return less_indx


# Поиск ближайшего меньшего справа
less_right = search_less(True)

# Поиск ближайшего меньшего слева
less_left = search_less(False)

# Расчёт площади
max_square = 0
for idx_hi, idx_less_right in less_right.items():
    idx_less_left = less_left[idx_hi]
    square = (idx_less_right - idx_less_left - 1)*lst[idx_hi]
    max_square = max(max_square, square)
print(max_square)
stdin.close()
