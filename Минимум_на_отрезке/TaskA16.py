# Решение с помощью дека за линейное время.
# В деке храним возрастающую последовательность кандидатов на минимум
# в будущем.
# В деке может находиться элемент, который выпал только на самом первом месте.
# Если то, что выпало из окна и то, что стоит на первом месте в деке
# (самый маленький элемент) не совпадает.
# То можно утверждать, что этого числа уже нет в деке.
# Потому, что меньший элемент уже вытолкнул данное число.
# Для реализации дека использовал класс deque() модуля collections.
from collections import deque

stdin = open("input.txt", "r")
n, k = list(map(int, stdin.readline().rstrip().split()))
lst = stdin.readline().rstrip().split()
dct = {}
stdin.close()
deck = deque()
answer = []
front = 0
for i, chank in enumerate(lst):
    num = int(chank)
# Пытался оптимизировать получение левой границы с помощью словаря,
# так как там O(1) на удаление и получение.
    if (i < k):
        dct[i] = num
    else:
        front = dct.pop(i - k)
        dct[i] = num
    if ((i >= k) and len(deck) and int(front) == deck[0]):
        # Удаляю минимум для прошлого окна.answer
        deck.popleft()

    if (len(deck) and deck[-1] <= num):
        # Добавляем кандидат в минимум.
        deck.append(num)
    else:
        # Удаляем те значения, которые никогда не будут минимумами.
        while len(deck) and deck[-1] > num:
            back = deck.pop()
        deck.append(num)

    if (not len(deck)):
        deck.append(num)
    # Добавляем ответ в список.
    if (i + 1 >= k):
        answer.append(str(deck[0]))
    prev = num

stdout = open('output.txt', 'w')
stdout.write('\n'.join(answer))
stdout.close()
