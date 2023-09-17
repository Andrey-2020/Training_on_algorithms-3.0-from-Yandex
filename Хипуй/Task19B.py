from typing import List


class Heap:
    heap_list = list()

    def Insert(self, k):
        self.heap_list.append(k)
        pos = len(self.heap_list) - 1
        while pos > 0 and self.heap_list[pos] > self.heap_list[(pos - 1) // 2]:
            self.heap_list[pos], self.heap_list[(pos - 1) // 2] =\
                self.heap_list[(pos - 1) // 2], self.heap_list[pos]
            pos = (pos - 1) // 2

    def Extract(self):
        ans = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        pos = 0
        while 2*pos + 2 < len(self.heap_list):
            max_son_index = 2*pos + 1
            if self.heap_list[2*pos + 2] > self.heap_list[max_son_index]:
                max_son_index = 2*pos + 2
            max_son_item = self.heap_list[max_son_index]
            if max_son_item > self.heap_list[pos]:
                self.heap_list[pos], self.heap_list[max_son_index] =\
                    max_son_item, self.heap_list[pos]
                pos = max_son_index
            else:
                break
        self.heap_list.pop()
        return ans


def read_input() -> List[int]:
    heapify = Heap()
    output = []
    with open('input.txt') as stdin:
        n = int(stdin.readline())
        while n:
            command = list(map(int, stdin.readline().rstrip().split()))
            if command[0] == 0:
                heapify.Insert(command[1])
            else:
                output.append(str(heapify.Extract()))
            n -= 1
    return output


if __name__ == '__main__':
    output = read_input()
    print('\n'.join(output))
