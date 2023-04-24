from collections import OrderedDict
from bisect import bisect_left
stdin = open('input.txt', 'r')

N = int(stdin.readline().rstrip())
pN = stdin.readline().rstrip().split(' ')
K = stdin.readline().rstrip()
pK = stdin.readline().rstrip().split(' ')


set_pN = OrderedDict.fromkeys(pN)
result = [int(item) for item in set_pN]
new_pN = sorted(result, key=lambda i: int(i))


for p_i in pK:
    pi = int(p_i)
    index_in_Diego = bisect_left(new_pN, pi)
    print(index_in_Diego)

stdin.close()
