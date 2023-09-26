def sum_of_cubes(n) -> int:
    dp = [0]*(n + 1)
    dp[1] = 1
    for x in range(2, n + 1):
        res = 10 ^ 7
        cubes = [i*i*i for i in range(int(x**(1/3)) + 1, 0, -1)]
        for cube in cubes:
            if x >= cube:
                res = min(res, dp[x - cube])
        dp[x] = res + 1
    return dp[-1]


def read_input() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    print(sum_of_cubes(read_input()))
