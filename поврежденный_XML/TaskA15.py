# Идея в замене каждого из N символов на каждый из символов алфавита.
# Строчные буквы латинского алфавита со спец. символами [/, <, >].
# Размер алфавита a = 26 + 3. Временная сложность O(a*N)
# Корректность проверяется за N с помощью стека.
# Общая сложность O(a*N^2)

def check_XML(lst):
    """Проверка валидности XML."""
    stack = []
    close_flag = False
    for char in lst:
        if (char == '<'):
            stack.append(char)
        elif (char == '/'):
            if (len(stack) < 2 or stack[-1] != '<'):
                return False
            if (close_flag):
                stack[-1] = ''.join([stack[-1]] + [char])
            close_flag = True
        elif (char == '>'):
            if (close_flag):
                if (len(stack) >= 2):
                    close = ''.join([stack.pop()] + [char])
                    open_tag = stack[-1]
                    if (close == open_tag):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                if (len(stack) == 0):
                    return False
                stack[-1] = ''.join([stack[-1]] + [char])
            close_flag = False
        else:
            if (len(stack) == 0 and char != '<'):
                return False

            stack[-1] = ''.join([stack[-1]] + [char])

    if (len(stack)):
        return False
    else:
        return True


def сhange_char_XML(chars, char, index):
    """Перебор всех символов."""
    copy_chars = chars.copy()
    check_XML(copy_chars)
    ask2 = 47
    while ask2 <= 90:
        copy_chars[index] = chr(ask2).lower()
        if (check_XML(copy_chars)):
            return copy_chars

        if (ask2 == 47):
            ask2 = 60
        elif (ask2 == 60):
            ask2 = 62
        elif (ask2 == 62):
            ask2 = 65
        elif (ask2 >= 65):
            ask2 += 1


if (__name__ == '__main__'):
    stack = []
    answer = None
    stdin = open('input.txt', 'r')
    chars = list(stdin.readline().rstrip())
    stdin.close()
    if (check_XML(chars)):
        print(check_XML(chars))
        answer = chars
    else:
        for i, char in enumerate(chars):
            answer = сhange_char_XML(chars, char, i)
            if (answer is not None):
                break
    if (answer is not None):
        print(''.join(answer))
