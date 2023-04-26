# Эта функция использует тот факт,
# что каждое другое целое число будет иметь по крайней мере одно число,
# кратное двум, без остатка.
stdin = open('input.txt', 'r')

A = (stdin.readline().rstrip())
B = (stdin.readline().rstrip())
C = (stdin.readline().rstrip())
days_second = 24*60*60


def get_seconds(time: str):
    hour, minutes, secs = map(int, time.split(":"))
    minutes = minutes + hour * 60
    return secs + minutes * 60


def time_format(seconds: int):
    sec = seconds % 60
    minutes = seconds // 60
    minute = minutes % 60
    hours = minutes // 60
    hour = hours % 24
    return f"{hour:02d}:{minute:02d}:{sec:02d}"


time_A = get_seconds(A)
time_B = get_seconds(B)
time_C = get_seconds(C)
if (time_C < time_A):
    time_C += days_second
delay = (time_C - time_A) / 2
if ((delay + 0.5) % 2 == 0 or (delay + 1.5) % 2 == 0):
    delay = delay + 0.5
else:
    delay = round(delay, 1)

exact_time = time_B + int(delay)
print(time_format(exact_time))
stdin.close()
