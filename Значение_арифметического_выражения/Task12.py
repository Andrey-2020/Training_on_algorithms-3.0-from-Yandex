# Преобразование исходных данных в список и минимальная проверка.
# Преобразование инфиксной нотации в постфиксную.
# Если ошибка при выполнении в except срабатывает вывод WRONG.

expr_lst = []
operators = ['+', '-', '*', '(', ')']

priorities = {'+': 1, '-': 1, '*': 2, '(': 0, ')': 0}

isWrong = False
isprevNumb = False
with open('input.txt') as stdin:
    isSpace = False
    # Преобразование исходных данных в список и минимальная проверка
    # на корректность
    for char in stdin.read():
        if (char == '\n'):
            continue
        if (not char.isnumeric() and (char not in operators) and char != ' '):
            print('WRONG')
            isWrong = True
            break
        if (char == ' '):
            isSpace = True
        elif (isSpace and isprevNumb and char.isnumeric()):
            print('WRONG')
            isWrong = True
            break
        if (char.isnumeric()):
            isprevNumb = True
            if (len(expr_lst) and expr_lst[-1].isnumeric()):
                expr_lst[-1] = ''.join([expr_lst[-1], char])
            else:
                expr_lst.append(char)
        if (char in operators):
            isSpace = False
            isprevNumb = False
            expr_lst.append(char)
postfixs = []
stack = []
if (not isWrong):
    try:
        # Преобразование инфиксной нотации в постфиксную
        for char in expr_lst:
            if (char not in operators):
                postfixs.append(int(char))
            else:
                if (char == '('):
                    stack.append(char)
                elif (char == ')'):
                    opeatorStack = stack.pop()
                    while opeatorStack != '(':
                        postfixs.append(opeatorStack)
                        opeatorStack = stack.pop()
                elif (len(stack) and
                      priorities[char] <= priorities[stack[-1]]):
                    while (len(stack) != 0 and
                           (priorities[char] <= priorities[stack[-1]])):
                        if (stack[-1] == '('):
                            break
                        lastChar = stack.pop()
                        postfixs.append(lastChar)
                    stack.append(char)
                else:
                    stack.append(char)
        if (len(stack)):
            for operator in stack[::-1]:
                postfixs.append(operator)
                stack.pop()
        expr_lst.clear()
        # Расчет суммы по постфиксной записи
        for char in postfixs:
            if (char not in operators):
                stack.append(char)
            else:
                after = stack.pop()
                if ('+' in char):
                    stack[-1] = stack[-1] + after
                elif ('-' in char):
                    stack[-1] = stack[-1] - after
                elif ('*' in char):
                    stack[-1] = stack[-1] * after
        print(*stack)
    except IndexError:
        print('WRONG')
