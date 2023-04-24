# Решение за время NlogN. Хотя я не уверен.
# Используется бинарный поиск отрезка в отсортиврованном списке.
# Удаление пересекающихся отрезков до первого непересекающегося.
# Время сортировки не учтено в сложности NlogN,
# возможно, этот способ даже хуже предыдущего.
from bisect import bisect_left
stdin = open('input.txt', 'r')

M = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())
systems = []
for _ in range(0, N):
    sectionStr = stdin.readline().rstrip()
    section = list(map(int, sectionStr.split(' ')))
    systems_no_cross = []
    index_cross = bisect_left(systems, section)
    while True:
        if (index_cross >= len(systems)):
            break
        if (section[0] <= systems[index_cross][1] and systems[index_cross][0] <= section[1]):
            systems.pop(index_cross)
        else:
            break
    if (index_cross - 1 >= 0 and (section[0] <= systems[index_cross - 1][1] and systems[index_cross - 1][0] <= section[1])):
        systems.pop(index_cross - 1)
    systems.append(section)
    systems = sorted(systems, key=lambda x: x[0])

print(len(systems))
stdin.close()
