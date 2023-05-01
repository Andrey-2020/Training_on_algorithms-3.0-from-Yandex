# Задача на стек
stdin = open("input.txt", "r")
N = int(stdin.readline().rstrip())
wagons = stdin.readline().rstrip().split(" ")
stack = []
i = 1
for wagon in wagons:
    num = int(wagon)
    stack.append(num)
    if (stack[-1] == i):
        while len(stack) and stack[-1] == i:
            stack.pop()
            i += 1
if (len(stack)):
    print("NO")
else:
    print("YES")
stdin.close()
