# Преобразование исходных данных в список.
# Вычисление арифметического выражения по постфиксной записи.

expr_lst = []
operators = ['+', '-', '*', '(', ')']

priorities = {'+': 1, '-': 1, '*': 2, '(': 0, ')': 0}

stdin = open('input.txt', 'r')
expr_postfixs = stdin.readline().rstrip().split(' ')
stack = []

expr_lst.clear()
# Расчет арифметического выражения по постфиксной записи
for char in expr_postfixs:
    if (char not in operators):
        stack.append(char)
    else:
        after = stack.pop()
        if ('+' in char):
            stack[-1] = int(stack[-1]) + int(after)
        elif ('-' in char):
            stack[-1] = int(stack[-1]) - int(after)
        elif ('*' in char):
            stack[-1] = int(stack[-1]) * int(after)
print(*stack)
