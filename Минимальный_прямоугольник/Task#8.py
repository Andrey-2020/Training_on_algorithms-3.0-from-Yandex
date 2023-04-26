stdin = open('input.txt', 'r')

K = int(stdin.readline().rstrip())
list_x = []
list_y = []
for _ in range(0, K):
    sectionStr = stdin.readline().rstrip()
    coor_x, coor_y = list(map(int, sectionStr.split(' ')))
    list_x.append(coor_x)
    list_y.append(coor_y)

print(min(list_x), min(list_y), max(list_x), max(list_y))
