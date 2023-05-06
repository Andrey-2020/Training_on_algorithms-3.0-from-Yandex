from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
        self.output = []

    def push(self, n):
        self.queue.append(n)
        self.output.append("ok")

    def front(self):
        if not self._isEmpty():
            self.output.append(self.queue[0])
        else:
            self.output.append("error")

    def pop(self):
        if not self._isEmpty():
            self.output.append(str(self.queue.popleft()))
        else:
            self.output.append("error")

    def _isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        self.output.append(str(len(self.queue)))

    def clear(self):
        self.queue.clear()
        self.output.append("ok")

    def exit(self):
        self.output.append("bye")
        return "\n".join(self.output)


if __name__ == '__main__':
    queue = Queue()
    outut_txt = open("output.txt", "w")
    with open('input.txt', 'r') as stdin:
        for line in stdin:
            command = line.rstrip().split()
            func = getattr(queue, command[0])
            if command[0] == "exit":
                outut_txt.write(func())
                break
            func(command[1]) if (command[0] == "push") else func()
    outut_txt.close()
