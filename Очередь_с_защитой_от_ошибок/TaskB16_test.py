class Queue:
    def __init__(self):
        self.max_size = 250
        self.queue = {i: 0 for i in range(self.max_size)}
        # creates a dict {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        self.front_pos = 0
        self.back_pos = 0
        self.output = []

    def push(self, n):
        if not self._isFull():
            self.queue[self.back_pos] = n
            self.output.append("ok")
            self.back_pos += 1
        else:
            self.front = 0
            self.back_pos = 0

    def front(self):
        if not self._isEmpty():
            self.output.append(self.queue[self.front_pos])
        else:
            self.output.append("error")

    def pop(self):
        if not self._isEmpty():
            self.output.append(str(self.queue[self.front_pos]))
            self.front_pos += 1
        else:
            self.output.append("error")

    def _isEmpty(self):
        return self.back_pos - self.front_pos == 0

    def _isFull(self):
        return self.back_pos - self.front_pos == self.max_size

    def size(self):
        self.output.append(str(self.back_pos - self.front_pos))

    def clear(self):
        self.queue.clear()
        self.front_pos = 0
        self.back_pos = 0
        self.output.append("ok")

    def exit(self):
        self.output.append("bye")
        with open("output.txt", "w") as stdout:
            stdout.writelines("\n".join(self.output))


if __name__ == '__main__':
    queue = Queue()
    with open('input.txt', 'r') as stdin:
        for line in stdin:
            command = line.rstrip().split()
            func = getattr(queue, command[0])
            if command[0] == "exit":
                func()
                break
            func(command[1]) if (command[0] == "push") else func()
