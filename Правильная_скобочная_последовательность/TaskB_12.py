stack = []
brakets_open = ['(', '[', '{']
brakets_close = [')', ']', '}']
brakets = {'(': ')', '[': ']', '{': '}'}
with open('input.txt', 'r') as stdin:
    for chank in stdin.read():
        if (chank != '\n' and chank in brakets_open):
            stack.append(chank)
        elif (len(stack) and chank != '\n' and chank in brakets_close):
            if (brakets[stack[-1]] != chank):
                break
            braket = stack.pop()
        elif (not len(stack) and chank in brakets_close):
            stack.append(chank)
            break
if (len(stack)):
    print("no")
else:
    print("yes")
