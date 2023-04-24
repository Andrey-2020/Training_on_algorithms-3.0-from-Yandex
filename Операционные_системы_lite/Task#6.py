# Неоптимальное решение за O(N^2). 
# Перебор и удаление пересекающихся отрезков через создание нового списка.
stdin = open('input.txt', 'r')

M = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())
systems = []
for _ in range(0, N):
    sectionStr = stdin.readline().rstrip()
    section = list(map(int, sectionStr.split(' ')))
    systems_no_cross = []
    for val in systems:
        if (not (section[0] <= val[1] and val[0] <= section[1])):
            systems_no_cross.append(val)
    systems = systems_no_cross.copy()
    systems.append(section)

print(len(systems))
stdin.close()
