from collections import deque
left = deque()
right = deque()
stdout = []
with open("input.txt", "r") as stdin:
    N = int(stdin.readline().rstrip())
    front = 0
    for i in range(N):
        command = stdin.readline().rstrip().split()
        if (command[0] == "+"):
            right.append(command[1])
        elif (command[0] == "*"):
            right.appendleft(command[1])
        else:
            stdout.append(left.popleft())
        if (len(left) < len(right)):
            left.append(right.popleft())

print("\n".join(stdout))
