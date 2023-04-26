# задача про математику
# Нашли в скольких подстроках встречается буква и перемножили количество
# перемножили количество до и после буквы
stdin = open('input.txt', 'r')

word = stdin.readline().rstrip()
stdin.close()
chars = list(word)
count_of_comb = {}
for i, char in enumerate(chars):
    if (not count_of_comb.get(char, False)):
        count_of_comb[char] = (len(chars) - i)*(i + 1)
    else:
        count_of_comb[char] += (len(chars) - i)*(i + 1)

sort_count = sorted(count_of_comb.items(), key=lambda x: ord(x[0]))
for char, count in sort_count:
    print(f'{char}: {count}')
