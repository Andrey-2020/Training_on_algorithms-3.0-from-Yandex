class Deque:
    buf_size = 100
    deque_front = list()
    deque_back = list()
    front_head = 0
    back_head = 0
    _size = 0

    deque_output = list()

    def push_front(self, n):
        """Добавить (положить) в начало дека новый элемент.
        Программа должна вывести ok."""
        self.__update()
        self.deque_front.append(int(n))
        self.deque_output.append("ok")
        self._size += 1

    def push_back(self, n):
        """Добавить (положить) в конец дека новый элемент.
        Программа должна вывести ok."""
        self.__update()
        self.deque_back.append(int(n))
        self.deque_output.append("ok")
        self._size += 1

    def pop_front(self):
        """"Извлечь из дека первый элемент.
        Программа должна вывести его значение."""
        self.__update()
        if (self.deque_front):
            self.deque_output.append(str(self.deque_front.pop()))
            self._size -= 1
        elif (self.deque_back and self.back_head != len(self.deque_back)):
            item = self.deque_back[self.back_head]
            self.deque_output.append(str(item))
            self.back_head += 1
            self._size -= 1
        else:
            self.deque_output.append("error")

    def pop_back(self):
        """Извлечь из дека последний элемент.
        Программа должна вывести его значение."""
        self.__update()
        if (self.deque_back):
            self.deque_output.append(str(self.deque_back.pop()))
            self._size -= 1
        elif (self.deque_front and self.front_head != len(self.deque_front)):
            item = self.deque_front[self.front_head]
            self.deque_output.append(str(item))
            self.front_head += 1
            self._size -= 1
        else:
            self.deque_output.append("error")

    def front(self):
        """Узнать значение первого элемента (не удаляя его).
        Программа должна вывести его значение."""
        self.__update()
        if (self.deque_front):
            item = self.deque_front[-1]
            self.deque_output.append(str(item))
        elif (self.deque_back and self.back_head != len(self.deque_back)):
            item = self.deque_back[self.back_head]
            self.deque_output.append(str(item))
        else:
            self.deque_output.append("error")

    def back(self):
        """Узнать значение последнего элемента (не удаляя его).
        Программа должна вывести его значение."""
        self.__update()
        if (self.deque_back):
            item = self.deque_back[-1]
            self.deque_output.append(str(item))
        elif (self.deque_front and self.front_head != len(self.deque_front)):
            item = self.deque_front[self.front_head]
            self.deque_output.append(str(item))
        else:
            self.deque_output.append("error")

    def size(self):
        """"Вывести количество элементов в деке."""
        self.deque_output.append(str(self._size))

    def __update(self):
        """Обновить списки, убрав лишние значения.
        Если размер списков превышает выделенный размер."""
        if (self._size == self.buf_size
            or self.front_head >= self.buf_size // 2
            or self.back_head >= self.buf_size // 2
                or not self._size):
            new_deque_back = list()
            new_deque_front = list()
            if len(self.deque_front) > self.front_head:
                new_deque_front = self.deque_front[self.front_head::]

            if len(self.deque_back) > self.back_head:
                new_deque_back = self.deque_back[self.back_head::]
            self.deque_front = new_deque_front
            self.deque_back = new_deque_back
            self._size = len(self.deque_front) + len(self.deque_back)
            self.front_head = 0
            self.back_head = 0

    def clear(self):
        """Очистить дек (удалить из него все элементы) и вывести ok."""
        self.deque_front.clear()
        self.deque_back.clear()
        self.front_head = 0
        self.back_head = 0
        self._size = 0
        self.deque_output.append("ok")

    def exit(self):
        """Программа должна вывести bye и завершить работу."""
        self.deque_output.append("bye")
        with open('output.txt', 'w') as stdout:
            stdout.write('\n'.join(self.deque_output))


if __name__ == '__main__':
    with open('input.txt', 'r') as stdin:
        deq = Deque()
        while (command := stdin.readline().rstrip().split())[0] != "exit":
            func = getattr(deq, command[0])
            if command[0] == "push_back" or command[0] == "push_front":
                func(command[1])
            else:
                func()
        getattr(deq, command[0])()
