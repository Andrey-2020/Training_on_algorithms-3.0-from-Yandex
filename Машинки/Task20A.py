from typing import List, Union
import heapq


def calc_min_number(n: int, k: int, toys: List[int]) -> int:
    nearest_toys = {}
    toys_floor = []
    playing = {}
    ans = 0
    for i, item in enumerate(reversed(toys)):
        toy = toys[len(toys) - i - 1]
        if not nearest_toys.get(toy, False):
            toys[len(toys) - i - 1] = (-len(toys)-1, toy)
            # -len(toys)-1 означает, что машинка больше не будет использована
        else:
            toys[len(toys) - i - 1] = (-nearest_toys.get(toy), toy)
        nearest_toys[toy] = (len(toys) - i - 1)

    for toy in toys:
        if not playing.get(toy[1], False):
            if len(playing) >= k:
                del_val = heapq.heappop(toys_floor)
                del playing[del_val[1]]
            heapq.heappush(toys_floor, toy)
            playing[toy[1]] = toy[0]
            ans += 1
        else:
            heapq.heappush(toys_floor, toy)

    return ans


def read_input() -> Union[int, int, List[int]]:
    toys = []
    with open('input.txt') as stdin:
        n, k, p = list(map(int, stdin.readline().strip().split()))
        while p:
            toys.append(int(stdin.readline()))
            p -= 1
    return n, k, toys


if __name__ == '__main__':
    n, k, toys = read_input()
    print(calc_min_number(n, k, toys))
