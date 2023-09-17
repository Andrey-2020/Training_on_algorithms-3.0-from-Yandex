import heapq
from typing import List


def min_fee(array) -> float:
    fee = 0
    while (len(array)) > 1:
        sum = heapq.heappop(array) + heapq.heappop(array)
        fee += sum*0.05
        heapq.heappush(array, sum)
    return fee


def read_input() -> List[int]:
    with open('input.txt') as stdin:
        _ = int(stdin.readline())
        array = list(map(int, stdin.readline().rstrip().split()))
    heapq.heapify(array)
    return array


if __name__ == '__main__':
    array = read_input()
    print(f"{min_fee(array):.2f}")
