# Задача предполагает использование кучи.
# Поддерживались 2 кучи минимумов. Одна для времени отправления.
# Другая для освободившихся мест в тупике.
import heapq
with open('input.txt') as stdin:
    K, N = map(int, stdin.readline().rstrip().split())
    time_out = []
    output = []
    ends = []

    is_output = True
    for count in range(1, N + 1):
        train_in, train_out = map(int, stdin.readline().rstrip().split())
        if (time_out and (train_in > time_out[0][0] or ends)):
            while (time_out and train_in > time_out[0][0]):
                end = heapq.heappop(time_out)
                heapq.heappush(ends, (end[1], train_out))
            end = heapq.heappop(ends)
            heapq.heappush(time_out, (train_out, end[0]))
            output.append(str(end[0]))
        else:
            if (len(time_out) + 1 > K):
                is_output = False
                print(f'{0} {count}')
                break
            heapq.heappush(time_out, (train_out, len(time_out) + 1))
            output.append(str(len(time_out)))
if (is_output):
    with open('output.txt', 'w') as stdout:
        stdout.write('\n'.join(output))
