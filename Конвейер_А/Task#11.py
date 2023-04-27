# Задача решена с помощью стека.
# Сравнивались значения в сортированном списке и в стеке.
stdin = open('input.txt', 'r')

N = int(stdin.readline().rstrip('\n'))
for _ in range(0, N):
    containers = list(map(float, stdin.readline().rstrip().split(' ')))
    K = int(containers.pop(0))
    sortStack = sorted(containers)
    stack = []
    isAswer = True
    i = 0
    j = 0
    k = 0
    while j < K:
        if (len(stack) and sortStack[j] == stack[-1]):
            stack.pop()
            j += 1
            continue
        container = containers[i]
        if (len(stack) and container > stack[-1]):
            isAswer = False
            break
        if (not sortStack[j] == container):
            stack.append(container)
            i += 1
        else:
            i += 1
            j += 1
    print(0) if (len(stack)) else print(1)

stdin.close()
