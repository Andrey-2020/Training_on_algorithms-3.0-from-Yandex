# Хорошесть - количество букв за которой идет следующия по алфавиту.
# Максимизировать хорошесть
# Пример abcab. Хорошесть 3
# Решение - минимум из количества букв которые есть у нас и следующей буквы по алфавиту

stdin = open('input.txt', 'r')
N = int(stdin.read(1))
inputText = stdin.read().split('\n')
maxPretty = 0
for i in range(1, len(inputText)):
    if (i + 2 < len(inputText)):
        maxPretty += min([int(inputText[i]), int(inputText[i+1])])

print(maxPretty)
