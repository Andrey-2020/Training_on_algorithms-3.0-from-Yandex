from typing import List, Union


class Heap:

    def heapify(self, arr, n, i):
        largest = i
        left_son = 2 * i + 1
        right_son = 2 * i + 2

        if left_son < n and arr[i] < arr[left_son]:
            largest = left_son

        if right_son < n and arr[largest] < arr[right_son]:
            largest = right_son

        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])

            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.heapify(arr, i, 0)
        return arr


def read_input() -> Union[int, List[int]]:
    with open('input.txt') as stdin:
        n = int(stdin.readline())
        array = list(map(int, stdin.readline().strip().split()))

    return n, array


if __name__ == '__main__':
    n, array = read_input()
    heap_sort = Heap().heapSort(array)
    print(*heap_sort)
