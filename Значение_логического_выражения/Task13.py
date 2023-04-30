# Преобразование исходных данных в список.
# Преобразование инфиксной нотации в постфиксную.
# Вычисление логического выражения по постфиксной записи.

expr_lst = []
operators = ['!', '&', '|', '^', '(', ')']

priorities = {'!': 4, '&': 3, '|': 2, '^': 2, '(': 1, ')': 1}

isWrong = True
isprevNumb = False
with open('input.txt') as stdin:
    for char in stdin.read():
        if (char == '\n'):
            continue
        else:
            expr_lst.append(char)

postfixs = []
stack = []

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
# Вычисление логического выражения по постфиксной записи
for char in postfixs:
    if (char not in operators):
        stack.append(char)
    else:

        if ('!' in char):
            stack[-1] = 1 * (not stack[-1])
        elif ('&' in char):
            after = stack.pop()
            stack[-1] = stack[-1] & after
        elif ('|' in char):
            after = stack.pop()
            stack[-1] = stack[-1] | after
        elif ('^' in char):
            after = stack.pop()
            stack[-1] = stack[-1] ^ after
print(*stack)
