from collections import deque


with open("input.txt") as stdin:
    first = deque(map(int, stdin.readline().rstrip().split()))
    second = deque(map(int, stdin.readline().rstrip().split()))

if (__name__ == "__main__"):
    count = 0
    while first and second and count < 10**6:
        count += 1
        card1 = first.popleft()
        card2 = second.popleft()
        if (card1 == 0 and card2 == 9):
            first.extend([card1, card2])
        elif (card1 == 9 and card2 == 0):
            second.extend([card1, card2])
        elif (card1 > card2):
            first.extend([card1, card2])
        else:
            second.extend([card1, card2])
    if (count >= 10**6):
        print("botva")
    else:
        print(f"second {count}") if not first else print(f"first {count}")
