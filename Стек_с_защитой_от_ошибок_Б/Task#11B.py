# Для моделирования стандартной структурой данных stack использовал класс.
# К методам обращался с помощью getattr.
# Позволяет получить значение атрибута объекта по его имени.
# Склеивали значения списка output_stack для более быстрого вывода результата.
# Это быстрее чем вызов print по отдельности

class Stack(object):
    stack = list()
    output_stack = list()

    def push(self, n):
        self.stack.append(n)
        self.output_stack.append('ok')

    def pop(self):
        """Удаляет из стека последний элемент."""
        """Программа должна вывести его значение."""
        if (len(self.stack)):
            self.output_stack.append(self.stack.pop())
        else:
            self.output_stack.append('error')

    def back(self):
        if (len(self.stack)):
            self.output_stack.append(self.stack[-1])
        else:
            self.output_stack.append('error')

    def size(self):
        """Программа должна вывести количество элементов в стеке."""
        self.output_stack.append(str(len(self.stack)))

    def clear(self):
        """Программа должна очистить стек и вывести ok."""
        self.stack.clear()
        self.output_stack.append('ok')

    def exit(self):
        """Программа должна вывести bye и завершить работу."""
        self.output_stack.append('bye')
        print("\n".join(self.output_stack))


if (__name__ == '__main__'):
    stdin = open('input.txt', 'r')
    command = stdin.readline().rstrip().split(' ')
    stack = Stack()
    while command[0] != 'exit':
        func = getattr(stack, command[0])
        if (command[0] == 'push'):
            func(command[1])
        else:
            func()
        command = stdin.readline().rstrip().split(' ')
    getattr(stack, command[0])()
