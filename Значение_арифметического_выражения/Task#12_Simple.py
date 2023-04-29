s = open('input.txt', 'r')
try:
    print(eval(s.readline()))
except:  # noqa
    print('WRONG')
s.close()
