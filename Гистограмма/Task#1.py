stdout = open('output.txt', 'w')

histogram_Dict = {}
string = ('')
max = 0
with open('input.txt', 'r', encoding='utf-8') as stdin:
    while True:
        char = stdin.read(1)
        if char == ' ' or char == '\n':
            continue
        if not histogram_Dict.get(char, False) and not char == '':
            histogram_Dict[char] = 1
        elif not char == '':
            histogram_Dict[char] += 1
        if histogram_Dict.get(char, 0) > max:
            max = histogram_Dict.get(char)
        if not char:
            break
printList = []
char = ''

histogram = dict(sorted(histogram_Dict.items(), key=lambda x: ord(x[0])))
for key, value in histogram.items():
    if key == '':
        continue
    char += key
    for i in range(0, max):
        if len(printList) < max:
            printList.append('')
        if (i < max-value):
            printList[i] = printList[i] + ' '
        else:
            printList[i] = printList[i] + '#'
printList.append(char)
histogram = "\n".join(printList)
stdout.write(histogram)
stdout.close()
