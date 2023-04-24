# Задача решена подбором подходящей формулы для вывода места Васи
import math
stdin = open('input.txt', 'r')

N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())
row_number_Petya = int(stdin.readline().rstrip())
place_Petya = int(stdin.readline().rstrip())

row_number_Vasya = row_number_Petya + K // 2
row_number_Vasya_forward = row_number_Petya - K // 2
if (K % 2 == 0):
    place_Vasya = place_Petya
else:
    if place_Petya == 2:
        place_Vasya = place_Petya - 1
        row_number_Vasya = row_number_Vasya + 1
    elif place_Petya == 1:
        row_number_Vasya_forward = row_number_Vasya_forward - 1
        place_Vasya = place_Petya + 1

if (row_number_Vasya > math.ceil(N / 2)):
    row_number_Vasya = row_number_Vasya_forward
elif (row_number_Petya - row_number_Vasya_forward < row_number_Vasya - row_number_Petya):
    row_number_Vasya = row_number_Vasya_forward

if (row_number_Vasya == math.ceil(N / 2) and N % 2 == 1 and place_Vasya == 2):
    if row_number_Vasya_forward < 1:
        row_number_Vasya = -1
    else:
        row_number_Vasya = row_number_Vasya_forward

if (row_number_Vasya > math.ceil(N / 2) or row_number_Vasya < 1):
    print(-1)
else:
    print(row_number_Vasya, place_Vasya)
stdin.close()
